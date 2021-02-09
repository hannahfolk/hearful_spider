# Hearful Spider Assignment
![GitHub repo size](https://img.shields.io/github/repo-size/hannahfolk/hearful_spider)
![GitHub contributors](https://img.shields.io/github/contributors/hannahfolk/hearful_spider)
![GitHub stars](https://img.shields.io/github/stars/hannahfolk/hearful_spider?style=social)
![GitHub forks](https://img.shields.io/github/forks/hannahfolk/hearful_spider?style=social)
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
    
This assignment is a web scraping exercise for my application to Hearful Hub. It uses Python, Scrapy, and MongoDB.
    
<a href="https://github.com/hannahfolk/hearful_spider"><strong>Explore the docs »</strong></a>
    
<a href="https://hannahfolk/github.io/hearful_spider">View Demo</a>
·
<a href="https://github.com/hannahfolk/hearful_spider/issues">Report Bug</a>
·
<a href="https://github.com/hannahfolk/hearful_spider/issues">Request Feature</a>
    
## Table of Contents
    
* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Contact](#contact)
* [License](#license)
* [Acknowledgements](#acknowledgements)
    
## About The Project
    
[![Products][product-screenshot1]]()
[![Reviews][product-screenshot2]]()


### Built With
      
* [Python](https://www.python.org/)
* [Scrapy](https://scrapy.org/)
* [MongoDB](https://www.mongodb.com/)    
    
### Prerequisites
    
* Python (version 3 or higher)
    
### Installation
    
1. Clone the repo inside a virtual environment
```sh
git clone https://github.com/hannahfolk/hearful_spider.git
```
2. Install PIP packages
```sh
pip install scrapy
pip install pymongo
```
    
    
## Usage
    
1. Run the `product_data` spider.
```sh
scrapy scrawl product_data
```
2. Run the `reviews` spider.
```sh
scrapy crawl reviews
```
Note: The `product_id` key is currently hard coded so you may need to copy it from the MongoDB and paste it into the `reviews` spider in the `product_id` property.
    
    
## Contact
    
If you want to contact me you can reach me at [hfolk25@gmail.com](hfolk25@gmail.com).
    
    
## License
        
This project uses the [MIT][license-url] license.
    

## Acknowledgements
      
* [YouTube - Human Code](https://www.youtube.com/watch?v=Wp6LRijW9wg)
* [YouTube - buildwithpython](https://www.youtube.com/watch?v=djfnjtYB2co)

[repo-size-shield]: https://img.shields.io/github/repo-size/hannahfolk/hearful_spider
[contributors-shield]: https://img.shields.io/github/contributors/hannahfolk/hearful_spider
[contributors-url]: https://github.com/hannahfolk/hearful_spider/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hannahfolk/hearful_spider
[forks-url]: https://github.com/hannahfolk/hearful_spider/network/members
[stars-shield]: https://img.shields.io/github/stars/hannahfolk/hearful_spider?style=social
[stars-url]: https://github.com/hannahfolk/hearful_spider/stargazers
[issues-shield]: https://img.shields.io/github/issues/hannahfolk/hearful_spider
[issues-url]: https://github.com/hannahfolk/hearful_spider/issues
[license-shield]: https://img.shields.io/badge/license-MIT-green
[license-url]: https://github.com/hannahfolk/hearful_spider/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/hannahfolk
[product-screenshot1]: images/screenshot1.jpg
[product-screenshot2]: images/screenshot2.png