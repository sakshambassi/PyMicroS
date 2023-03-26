# PyMicroS
Micro-service with text analysis services


## Testing
To run unittests do:
```
bash run_test.sh
```

## Run Microservice

### Docker build
First build docker image using:
```
docker build -t pymicros-app .
```

### Start the app
Next, start the container using:
```
docker-compose up
```

Access the microservice on `http://127.0.0.1:5001`

## Endpoints

### POST /analyze-text

Request
```
{
  "service": "bigram",
  "text": "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again."
}
```

Response

```
{
    "result":
        [
            ["quick", "the"],
            ["brown", "quick"],
            ["brown", "fox"],
            ["fox", "jumps"],
            ["jumps", "over"],
            ["over", "the"],
            ["lazy", "the"],
            ["dog", "lazy"],
            ["again", "and"],
            ["again", "dog"]
        ]
}
```

Request
```
{
  "service": "word-count",
  "text": "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again and again."
}
```
Response
```
{
  "result": {
    "the": 4,
    "quick": 2,
    "brown": 2,
    "fox": 2,
    "jumps": 2,
    "over": 2,
    "lazy": 2,
    "dog": 2,
    "again": 2,
    "and": 1
  }
}
```