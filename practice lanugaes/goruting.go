package main

import (
	"fmt"
	"time"
)

func main() {
	go count("fish")
	count("dog")
}
func count(s string) {
	for i := 1; true; i++ {
		fmt.Println(i, s)
		time.Sleep(500 * time.Millisecond)
	}
}
