#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <uriparser/Uri.h>

#include <time.h>

int main() {
    UriParserStateA state;
    UriUriA uri;


    state.uri = &uri;

    if (uriParseUriA(&state, "http://банки.рф") != URI_SUCCESS) {
       uriFreeUriMembersA(&uri);
    }

    uriFreeUriMembersA(&uri);
    // uriFreeUriMembersA(&uri);
    // printf("absolutePath: %d\n", uri.absolutePath);
    // printf("scheme after Last: %s\n", uri.scheme.afterLast);
    // printf("scheme first: %s\n", uri.scheme.first);
    // printf("fragment after last: %s\n", uri.fragment.afterLast);
    // printf("fragment first: %s\n", uri.fragment.first);
    // printf("hostData ip 4: %s\n", uri.hostData.ip4->data);
    // printf("hostData ip6: %s\n", uri.hostData.ip6->data);
    // printf("hostData ipFuture afterLast: %s\n", uri.hostData.ipFuture.afterLast);
    // printf("hostData ipFuture first: %s\n", uri.hostData.ipFuture.first);
    printf("host text after Last: %s\n", uri.hostText.afterLast);
    printf("host text first: %s\n", uri.hostText.first);
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


    // double time_elapsed;
    //
    // FILE* fp;
    // char buffer[255];
    //
    // fp = fopen("chromiumUrls.txt", "r");
    //
    // while (fgets(buffer, 255, (FILE*) fp)) {
    //     clock_t start, end;
    //
    //     UriParserStateA state;
    //     UriUriA uri;
    //     // start
    //     start = clock();
    //
    //     state.uri = &uri;
    //
    //     if (uriParseUriA(&state, buffer) != URI_SUCCESS) {
    //         uriFreeUriMembersA(&uri);
    //     }
    //
    //     uriFreeUriMembersA(&uri);
    //     end = clock();
    //
    //     time_elapsed += ((double) (end - start) / CLOCKS_PER_SEC);
    //
    // }
    //
    // fclose(fp);
    //
    // printf("time elapsed for this program is: %f\n", time_elapsed);
    // return 0;
}
