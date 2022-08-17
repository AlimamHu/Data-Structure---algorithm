package main

import (
	"fmt"
)

func main() {
	// fmt.Println(http.Get("https://jsonplaceholder.typicode.com/posts/1" + "<script>alert()</script>"))
	// file, err := os.Open("finder.txt")
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}
}
