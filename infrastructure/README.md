# Run Redis for local development

Redis stores encrypted OAuth registrations, transactions, and grants. Docker Compose starts Redis and makes it available to the host at `127.0.0.1:6379`. [Compose file](compose.yml)

## Start Redis

1. From the repository root, open the infrastructure directory.

   ```sh
   cd infrastructure
   ```

2. Create the local settings file. An existing file is preserved.

   ```sh
   cp -n .env.example .env
   ```

3. Generate a password for a new installation.

   ```sh
   openssl rand -hex 32
   ```

4. Set `REDIS_PASSWORD` in `infrastructure/.env` to that value. The local server and the Compose health check use this password.
5. Start Redis.

   ```sh
   docker compose up -d --wait
   ```

6. Check the container status.

   ```sh
   docker compose ps
   ```

   Expect the `redis` service to report `healthy`.


## Stop Redis

From `infrastructure/`, run the following command.

```sh
docker compose down
```

The named volume retains the append-only log and snapshots across restarts and container replacement. Keep this volume and the MCP encryption key to retain access to the grants.

## Redis license

Compose specifies `redis:8.10.3-alpine`. Redis offers Redis 8 under AGPLv3, RSALv2, or SSPLv1. The MCP server connects to Redis as a separate process. If you distribute Redis under AGPLv3, its notice and corresponding-source terms apply. Section 13 covers network use of a modified Redis version. [Redis licensing](https://redis.io/legal/licenses/) · [AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html)
