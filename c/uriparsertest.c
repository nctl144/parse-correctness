#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <uriparser/Uri.h>

#include <time.h>

int main() {

    // printf("absolutePath: %d\n", uri.absolutePath);
    // printf("scheme after Last: %s\n", uri.scheme.afterLast);
    // printf("scheme first: %s\n", uri.scheme.first);
    // printf("fragment after last: %s\n", uri.fragment.afterLast);
    // printf("fragment first: %s\n", uri.fragment.first);
    // printf("hostData ip 4: %s\n", uri.hostData.ip4->data);
    // printf("hostData ip6: %s\n", uri.hostData.ip6->data);
    // printf("hostData ipFuture afterLast: %s\n", uri.hostData.ipFuture.afterLast);
    // printf("hostData ipFuture first: %s\n", uri.hostData.ipFuture.first);
    // printf("host text after Last: %s\n", uri.hostText.afterLast);
    // printf("host text first: %s\n", uri.hostText.first);
    // printf("owner: %d\n", uri.owner);
    //
    // // ask about this later
    // // printf("pathHead afterLast %s\n", uri.pathHead->text.afterLast);
    // // printf("pathHead first %s\n", uri.pathHead->text.first);
    // // printf("pathTail afterLast %s\n", uri.pathTail->text.afterLast);
    // // printf("pathTail first %s\n", uri.pathTail->text.first);
    //
    // printf("query afterLast: %s\n", uri.query.afterLast);
    // printf("query First: %s\n", uri.query.first);

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
    //     printf("url: %s", scheme_list[j]);
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

        UriParserStateA state;
        UriUriA uri;

        state.uri = &uri;

        if (uriParseUriA(&state, input_url_buffer) != URI_SUCCESS) {
            uriFreeUriMembersA(&uri);
        }

        uriFreeUriMembersA(&uri);

        if (strncmp(scheme_list[counter], uri.scheme.first, strlen(scheme_list[counter])) != 0) {
            printf("unmatched scheme: %s, at index: %d\n", input_url_buffer, counter);
        }

        if (strncmp(netloc_list[counter], uri.hostText.first, strlen(netloc_list[counter])) != 0) {
            printf("unmatched netloc: %s, at index: %d\n", input_url_buffer, counter);
        }

        // printf("1 %s, 2%s\n", scheme_list[counter], uri.scheme.first);
        // printf("host text after Last: %s\n", uri.hostText.afterLast);
        // printf("host text first: %s\n", uri.hostText.first);
        counter += 1;
    }

    fclose(input_url);

    printf("the program has finished :)\n");
    return 0;
}
