# FastAPI AWS Lambda

This is a simple example FastAPI application that pretends to be a bookstore.

# Deploying FastAPI to AWS Lambda

We'll need to modify the API so that it has a Lambda handler. Use Mangum:

```python
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)
```

We'll also need to install the dependencies into a local directory so we can zip it up.

```bash
pip install -t python -r requirements.txt
```

We now need to zip it up.

```bash
(cd python; zip ../python.zip -r .)
```
