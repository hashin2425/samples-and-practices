FROM golang:latest

WORKDIR /app

COPY go.mod .
COPY main.go .
COPY templates/ ./templates/

RUN go mod download

RUN go build -o main .

EXPOSE 8080

CMD ["./main"]
