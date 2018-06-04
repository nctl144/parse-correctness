#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <uriparser/Uri.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#include <time.h>

#define RANGE(x)  (int)((x).afterLast-(x).first), ((x).first)

int main() {

    /*
    *
    Read the input files
    */
    FILE* scheme_url;

    char scheme_url_buffer[255];
    char scheme_list[409][255];

    scheme_url = fopen("scheme-url.txt", "r");
    int index = 0;
    while (fgets(scheme_url_buffer, 255, (FILE*) scheme_url)) {
        strcpy(scheme_list[index], scheme_url_buffer);
        int i = 0;
        for (i = 0; i < strlen(scheme_list[index]); i++) {
            if (scheme_list[index][i] == '\n') {
                scheme_list[index][i] = '\0';
            }
        }
        index += 1;
    }

    fclose(scheme_url);


    FILE* netloc_url;

    char netloc_url_buffer[255];
    char netloc_list[409][255];

    netloc_url = fopen("netloc-url.txt", "r");
    int index_netloc = 0;
    while (fgets(netloc_url_buffer, 255, (FILE*) netloc_url)) {
        strcpy(netloc_list[index_netloc], netloc_url_buffer);
        int i = 0;
        for (i = 0; i < strlen(netloc_list[index_netloc]); i++) {
            if (netloc_list[index_netloc][i] == '\n') {
                netloc_list[index_netloc][i] = '\0';
            }
        }
        index_netloc += 1;
    }

    fclose(netloc_url);

    // int j;
    // for (j = 0; j < 409; j++) {
    //     printf("url: %s", netloc_list[j]);
    // }


    /*
    *
    Read the URL input files
    */
    FILE* input_url;

    char input_url_buffer[255];
    int counter = 0;
    input_url = fopen("input-url.txt", "r");
    while (fgets(input_url_buffer, 255, (FILE*) input_url)) {
        int i = 0;

        for (i = 0; i < strlen(input_url_buffer); i++) {
            if (input_url_buffer[i] == '\n') {
                input_url_buffer[i] = '\0';
            }
        }

        UriParserStateA state;
        UriUriA uri;

        state.uri = &uri;

        if (uriParseUriA(&state, input_url_buffer) != URI_SUCCESS) {
            uriFreeUriMembersA(&uri);
        }

        // scheme test
        if (uri.scheme.first) {
            char scheme[255];
            sprintf(scheme, "%.*s", RANGE(uri.scheme));

            if (strcmp(scheme_list[counter], scheme) != 0) {
                printf("unmatched scheme: %s, at index: %d\n", input_url_buffer, counter);
            }
		}

        if (uri.hostText.first) {
            char host[255];
			sprintf(host, "%.*s", RANGE(uri.hostText));

            if (strcmp(netloc_list[counter], host) != 0) {
                printf("unmatched netloc: %s, the result is: %s, while it should be: %s\n", input_url_buffer, host, netloc_list[counter]);
            }
		}

        counter += 1;

        uriFreeUriMembersA(&uri);
    }

    fclose(input_url);

    printf("the program has finished :)\n");
    return 0;
}
