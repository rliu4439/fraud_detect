Build using `docker build -f Dockerfile -t fraud-detect-api:latest .` in the /app directory

Run in docker using `docker run -p 5000:5000 fraud-detect-api`

Run in Kubernetes with `kubectl apply -f deployment.yaml`

Example input
```
curl http://localhost:5000/score \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"X":  [  -1.35980713,  -0.07278117,   2.53634674,
         1.37815522,  -0.33832077,   0.46238778,   0.23959855,
         0.0986979 ,   0.36378697,   0.09079417,  -0.55159953,
        -0.61780086,  -0.99138985,  -0.31116935,   1.46817697,
        -0.47040053,   0.20797124,   0.02579058,   0.40399296,
         0.2514121 ,  -0.01830678,   0.27783758,  -0.11047391,
         0.06692807,   0.12853936,  -0.18911484,   0.13355838,
        -0.02105305],
"amount_time": [0, 149.62]}'
```
