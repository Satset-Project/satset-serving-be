# SATSET Backend Service

Backend service of Satset.

## Prerequisites

- [Python](https://www.python.org/) 3.10 or higher
- [FastAPI](https://fastapi.tiangolo.com/) 0.104.1 or higher
- [Docker](https://www.docker.com/) 24.0.7 or higher
- [Docker Compose](https://docs.docker.com/compose/) 2.15.1 or higher

## Storage

- Cloud Storage

## Infrastructure

- Google Cloud Platform

## Folder Structure

```
.
├── app/
│   ├── dto.py
│   ├── main.py
│   ├── recommendation.py
│   └── utils.py
├── .dockerignore
├── .env
├── .env.example
├── .gitignore
├── Docker-compose.yml
├── Dockerfile
├── notebook.ipynb
├── README.md
└── requirements.txt
```

### Structure Explanation

- `app` is the source of backend service
- `main.py` on `app` is the entry point for the service
- create your own `.env` based on `.env.example` key provided

### How to Install

1. Clone this repo, `cd` to the cloned repo and checkout to `dev`
   ```bash
   git clone https://github.com/Satset-Project/satset-serving-be.git
   cd satset-serving-be
   ```
2. Update your .env

   ```bash
   on env TECHNICIANS_DF_URL, you must be deploy buckect technicians.csv and using the public url
   ```

3. Run for the first time
   - Using FastAPI
   ```bash
   cd app
   pip install fastapi==0.95.2 uvicorn==0.21.1 pandas==2.0.1 numpy==1.26.4 tensorflow==2.16.1 scikit-learn==1.5.0 starlette==0.27.0 pydantic==1.10.7 python-dotenv==1.0.1
   fastapi dev main.py
   ```
   - Dockerfile
   ```bash
   docker compose up --build
   ```

## API Endpoints

List of available endpoints:

### POST

<details>
  <summary><code>POST /recommend/content-based/</code> - Predict base content.</summary><br>

| Name         | Params | Required     | Type     | Description                                                        |
| ------------ | ------ | ------------ | -------- | ------------------------------------------------------------------ |
| `user_skill` | Query  | **required** | `string` | The province of skills technicians. Example `plumbing maintenance` |

**Response**

```json
{
  "status": true,
  "code": 200,
  "message": "OK",
  "data": {
    "technicianid": 85,
    "name": "Yoga Adika Narpati",
    "phonenumber": 6282753036164,
    "email": "yoganarpati@gmail.com",
    "skills": "Plumbing Maintenance, Washing Machine Repair",
    "experience": 14,
    "certifications": "Sertifikat Kompetensi BNSP Teknisi Plumbing & Drainase",
    "address": "Jl. Ahmad Dahlan No. 52",
    "location": "Bengkulu",
    "ratingsreceived": 4.5
  }
}
```

</details>

<details>
  <summary><code>POST /recommend/collaborative/</code> - Predict base collaborative.</summary><br>

| Name      | Params | Required     | Type     | Description                          |
| --------- | ------ | ------------ | -------- | ------------------------------------ |
| `user_id` | Query  | **required** | `string` | The province of user id. Example `5` |

**Response**

```json
{
  "status": true,
  "code": 200,
  "message": "OK",
  "data": {
    "technicianid": 125,
    "name": "Nrima Fujiati",
    "phonenumber": 6289850655077,
    "email": "nrimafujiati@gmail.com",
    "skills": "Computer Installation, AC Maintenance",
    "experience": 6,
    "certifications": "Sertifikat Kompetensi BNSP Teknisi Komputer Spesialis Senior",
    "address": "Jalan Suniaraja No. 9",
    "location": "Padang",
    "ratingsreceived": 3.6
  }
}
```

</details>

<details>
  <summary><code>POST /recommend/hybrid/</code> - Predict base hybrid.</summary><br>

| Name         | Params | Required     | Type     | Description                                                        |
| ------------ | ------ | ------------ | -------- | ------------------------------------------------------------------ |
| `user_id`    | Query  | **required** | `string` | The province of user id. Example `150`                             |
| `user_skill` | Query  | **required** | `string` | The province of skills technicians. Example `plumbing maintenance` |

**Response**

```json
{
  "status": true,
  "code": 200,
  "message": "OK",
  "data": {
    "technicianid": 74,
    "name": "Balidin Hartana Nurdiyanti",
    "phonenumber": 6281672402650,
    "email": "balidinnurdiyanti@gmail.com",
    "skills": "AC Maintenance, Computer Maintenance",
    "experience": 13,
    "certifications": "Sertifikasi Profesi Teknik Pendingin dan Tata Udara",
    "address": "Gg. Veteran No. 54",
    "location": "Bukittinggi",
    "ratingsreceived": 4.1
  }
}
```

</details>

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
