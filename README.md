## Use of decorator and meta function

While I haven't used it directly, this is an easy use case of decorators and meta functions that I thought of and implemented. 

Our code used a correlation ID, a unique code for each request, which gets attached onto HTTP calls for traceability and observability. Now, thus far, we used to add this onto our HTTP call methods into the metadata

But the obvious challenge was that we needed to add this to the request body, and since we don't make explicit get calls and instead, used a generic service, the variance of the correlation id was pretty limited.

Through the use of decorators, I've tried to ensure that we have a custom correlation ID for the calls, at method level, which can further be customized according to, say, types of user actions, or stages of the request
