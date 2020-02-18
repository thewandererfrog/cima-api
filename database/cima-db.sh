docker run -it -e POSTGRES_USER=cima -e POSTGRES_PASSWORD=cima -v /tmp:/tmp -v database:/var/lib/postgresql/data -p 5432:5432 postgres
