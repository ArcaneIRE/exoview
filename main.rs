use reqwest::blocking::Client;
use std::error::Error;
use std::fs::File;
use std::io::Write; 

fn main() -> Result<(), Box<dyn Error>> {
    let client = Client::new();

    // The ADQL query to search for stars within 100 parsecs
    let query = r#"
        SELECT hostname, ra, dec, sy_dist
        FROM ps
        WHERE 1=CONTAINS(
            POINT('ICRS', ra, dec), 
            CIRCLE('ICRS', 19.4955, -45.7883, 100.0/620.0)
        )
        AND sy_dist IS NOT NULL
    "#;

    let response = client.get("https://exoplanetarchive.ipac.caltech.edu/TAP/sync")
        .query(&[
            ("REQUEST", "doQuery"),
            ("LANG", "ADQL"),
            ("QUERY", query),
            ("FORMAT", "json"),  
        ])
        .send()?;

    let body = response.text()?;

    let mut file = File::create("stars_within_100_parsecs.json")?;

    file.write_all(body.as_bytes())?;

    println!("Data written to stars_within_100_parsecs.json");

    Ok(())
}
