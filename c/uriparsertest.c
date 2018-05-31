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

    FILE* scheme_url;

    char scheme_url_buffer[255];
    char scheme_list[409][255];

    scheme_url = fopen("scheme-url.txt", "r");
    int index = 0;
    while (fgets(scheme_url_buffer, 255, (FILE*) scheme_url)) {
        strcpy(scheme_list[index], scheme_url_buffer);

        index += 1;
    }

    int i;

    for (i = 0; i < 409; i++) {
        printf("%s", scheme_list[i]);
    }

    fclose(scheme_url);

    FILE* input_url;

    char input_url_buffer[255];
    input_url = fopen("input-url.txt", "r");
    while (fgets(input_url_buffer, 255, (FILE*) input_url)) {
        // UriParserStateA state;
        // UriUriA uri;

        // state.uri = &uri;
        //
        // if (uriParseUriA(&state, input_url_buffer) != URI_SUCCESS) {
        //     uriFreeUriMembersA(&uri);
        // }
        //
        // uriFreeUriMembersA(&uri);

    }

    fclose(input_url);

    printf("the program has finished :)");
    return 0;
}
