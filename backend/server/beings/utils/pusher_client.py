import pusher

pusher_client = pusher.Pusher(
    app_id='285567',
    key='76e36dc13c40f972a6d3',
    secret='e0eec9e78c33e77b9802',
    cluster='eu',
    ssl=True
)

# pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})