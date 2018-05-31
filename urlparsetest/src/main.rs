extern crate url;

use url::{Url, Host};
use std::fs::File;
use std::io::Read;


fn lines_from_file(filename: &str) -> Vec<String> {
    let mut file = match File::open(filename) {
        Ok(file) => file,
        Err(_) => panic!("no such file"),
    };
    let mut file_contents = String::new();
    file.read_to_string(&mut file_contents)
        .ok()
        .expect("failed to read!");
    let lines: Vec<String> = file_contents.split("\n")
        .map(|s: &str| s.to_string())
        .collect();
    lines
}

// fn import_data(filename: &str, list: &mut Vec<str>) {
//     for scheme in lines_from_file(filename) {
//         list.push(scheme);
//     }
// }

fn main() {

    let file_inputurl = "input-url.txt";
    let file_scheme = "scheme-url.txt";
    let file_netloc = "netloc-url.txt";

    let mut scheme_list = Vec::new();
    let mut netloc_list = Vec::new();
    let mut index = 0;

    for scheme in lines_from_file(file_scheme) {
        scheme_list.push(scheme);
    }

    for netloc in lines_from_file(file_netloc) {
        netloc_list.push(netloc);
    }

    for link in lines_from_file(file_inputurl) {

        let _issue_list_url = Url::parse(&link)
            .expect("Error while handling the issue_list_url");

        let url_scheme = _issue_list_url.scheme();
        let url_netloc = _issue_list_url.host_str();
        let mut url_netloc_str = "";

        if url_netloc.is_some() {
            url_netloc_str = url_netloc.unwrap()
        }

        if url_scheme != scheme_list[index] {
            println!("unmatched scheme, input is {}", link);
        }

        if url_netloc_str != netloc_list[index] {
            println!("unmatched netloc, input is {}", link);
        }

        index += 1;
        // println!("base url {}", link);
        // println!("username {:?}", _issue_list_url.username()); // ''
        // println!("password {:?}", _issue_list_url.password()); // None
        // println!("hoststr {:?}", _issue_list_url.host_str()); // Some("github.com")
        // println!("host {:?}", _issue_list_url.host()); // Some(Host::Domain("github.com")
        // println!("port {:?}", _issue_list_url.port()); // None
        // println!("path {}", _issue_list_url.path()); // "/rust-lang/rust/issues"
        // println!("path segments {:?}", _issue_list_url.path_segments().map(|c| c.collect::<Vec<_>>())); // Some(vec!["rust-lang", "rust", "issues"])
        // println!("query {:?}", _issue_list_url.query()); // Some("labels=E-easy&state=open")
        // println!("fragment {:?}", _issue_list_url.fragment()); // None
        // // println!(!_issue_list_url.cannot_be_a_base());
    }
    println!("program is finished :)");
}
