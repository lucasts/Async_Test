app = proc do |env|
  [
    200,          # Status code
    {             # Response headers
      'Content-Type' => 'text/html',
      'Content-Length' => '11',
    },
    ['Hello World']        # Response body
  ]
end

# You can install Rack middlewares
# to do some crazy stuff like logging,
# filtering, auth or build your own.
use Rack::CommonLogger

run app

