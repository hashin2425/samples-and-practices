package main

import (
	"html/template"
	"log"
	"net/http"
	"time"
)

type PageData struct {
	Time string
}

func main() {
	http.HandleFunc("/", homePage)
	log.Println("Server starting on port 8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func homePage(w http.ResponseWriter, r *http.Request) {
	template, err := template.ParseFiles("templates/index.html")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	data := PageData{
		Time: time.Now().Format("2006-01-02 15:04:05"),
	}

	err = template.Execute(w, data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}