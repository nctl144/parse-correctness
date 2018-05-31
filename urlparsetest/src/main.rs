extern crate url;
extern crate time;

use url::{Url, Host};
use std::fs::File;
use time::{Duration, PreciseTime};

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

fn main() {
    // --snip--
    let filename = "urls.txt";

    let mut totaltime = 0;

    for link in lines_from_file(filename) {
        let start = PreciseTime::now();
        let _issue_list_url = Url::parse(&link)
            .expect("Error while handling the issue_list_url");

        let end = PreciseTime::now();
        // println!("base url {}", link);
        // println!("scheme {}", _issue_list_url.scheme()); // https
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
        totaltime += start.to(end).num_microseconds().unwrap();
    }

    println!("Total execution time: {}", totaltime); // 16 seconds

    // let _issue_list_url = Url::parse("http://example.org/test?")
    //     .expect("Error while handling the issue_list_url");
    //
    // println!("query {:?}", _issue_list_url.query());
}
