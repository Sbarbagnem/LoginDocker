import conu

PORT = 8082

with conu.DockerBackend() as backend:
  image = backend.ImageClass("app_container")
  options = ["-p", "8082:8082"]
  container = image.run_via_binary(additional_opts=options)
  
  try:
    # Check that the container is running and wait for the flask application to start.
    assert container.is_running()
    container.wait_for_port(PORT)
    
    # Run a GET request on / port 5000.
    http_response = container.http_request(path="/", port=PORT)
    
    # Check the response status code is 200
    assert http_response.ok

    # Get the logs from the container
    logs = [line for line in container.logs()]
    # Check the the Flask application saw the GET request.
    assert b'"GET / HTTP/1.1" 200 -' in logs[-1]

  finally:
    container.stop()
    container.delete()