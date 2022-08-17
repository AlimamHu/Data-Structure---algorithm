package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"time"
)

func file_opener(s string) {
	file, err := os.Open("test.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		time.Sleep(10 * time.Second)
		request_url(s + scanner.Text()) // this area we add "url" + "script" |  song--> url + script
		// fmt.Println(http.Get("www.google.com/" + scanner.Text()))
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
func request_url(s string) { // function for request
	resp, err := http.Get(s)
	if err != nil {
		print(err)
	}

	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		print(err)
	}

	fmt.Print(string(body))

}
func main() {

	file_opener("https:www.google.com/")
	// request_url()
}
