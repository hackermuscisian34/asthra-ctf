FROM python:3.9-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM  python:3.9-slim

WORKDIR  /app

# Create a non-root user
RUN useradd -m -r -s /bin/bash ctfuser


# Copy files from builder
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY app.py .

# Create necessary directories and files
RUN mkdir -p /usr/local/share/.hidden /opt/.keys && \
    # Create flag file
    echo "flag{astra_ctf_2024_y0u_f0und_m3}" > /usr/local/share/.hidden/flag.txt && \
    # Create secret key file
    echo "s3cr3t_k3y_f0r_d3crypt10n" > /opt/.keys/secret_key.txt && \
    # Create binary file
    echo '#!/bin/bash\necho "Binary executed successfully"' > /usr/local/bin/binary && \
    # Set permissions
    chmod 600 /opt/.keys/secret_key.txt && \
    chmod 755 /usr/local/bin/binary && \
    chown -R root:root /opt/.keys && \
    chown -R root:root /usr/local/share/.hidden

# Create a false flag
RUN echo "flag{nice_try_but_not_here}" > /flag.txt && \
    chmod 644 /flag.txt

USER ctfuser
EXPOSE 80

ENTRYPOINT ["python", "app.py"]