#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <uriparser/Uri.h>


int main() {
    UriParserStateA stateA;
    const char * ref = "../TWO";
    const char * base = "file:///one/two/three";
    const char * expected = "file:///one/TWO";
    bool add = true;
    bool domainRootMode = false;

    // Base
    UriUriA baseUri;
    stateA.uri = &baseUri;
    int res = uriParseUriA(&stateA, base);
    if (res != 0) {
        return false;
    }

    // Rel
    UriUriA relUri;
    stateA.uri = &relUri;
    res = uriParseUriA(&stateA, ref);
    if (res != 0) {
        uriFreeUriMembersA(&baseUri);
        return false;
    }

    // Expected result
    UriUriA expectedUri;
    stateA.uri = &expectedUri;
    res = uriParseUriA(&stateA, expected);
    if (res != 0) {
        uriFreeUriMembersA(&baseUri);
        uriFreeUriMembersA(&relUri);
        uriFreeUriMembersA(&expectedUri);
        return false;
    }

    // Transform
    UriUriA transformedUri;
    if (add) {
        res = uriAddBaseUriA(&transformedUri, &relUri, &baseUri);
    } else {
        res = uriRemoveBaseUriA(&transformedUri, &relUri, &baseUri,
                domainRootMode ? URI_TRUE : URI_FALSE);
    }
    if (res != 0) {
        uriFreeUriMembersA(&baseUri);
        uriFreeUriMembersA(&relUri);
        uriFreeUriMembersA(&expectedUri);
        uriFreeUriMembersA(&transformedUri);
        return false;
    }

    const bool equal = (URI_TRUE == uriEqualsUriA(&transformedUri, &expectedUri));
    char transformedUriText[1024 * 8];
    char expectedUriText[1024 * 8];
    uriToStringA(transformedUriText, &transformedUri, 1024 * 8, NULL);
    uriToStringA(expectedUriText, &expectedUri, 1024 * 8, NULL);
    printf("\n\n\nExpected: \"%s\"\nReceived: \"%s\"\n\n\n", expectedUriText, transformedUriText);

    uriFreeUriMembersA(&baseUri);
    uriFreeUriMembersA(&relUri);
    uriFreeUriMembersA(&expectedUri);
    uriFreeUriMembersA(&transformedUri);

    return 0;

    // testAddOrRemoveBaseHelper("/../g", "http://a/b/c/d;p?q", "http://a/g", true, false);
}
