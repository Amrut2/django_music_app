<body style="background-color: #030303">
  

{% for i in song %}
<div class="container" style = "padding-left : 12%; padding-top:2%;margin:2%;background-color: #030303 ">
<div class="card mb-3" style="max-width: 940px; padding:3%;">
  <div class="row g-0" style="paddin-left:10px;">
    <div class="col-md-4">
      <img src="{{i.image.url}}" class="img-fluid rounded-start" alt="..." style="width:200px">
    </div>
    <div class="col-md-8">
      <div class="card-body">
          <p class="card-title"><b>Name:</b> {{i.name}}</p>
          <p class="card-text"><b>Singer:</b> {{i.singer}}</p>
        <a href="/musicbeatapp/songs/{{i.song_id}}"><button class= "btn btn-outline-danger">Listen Songs</button></a>
      </div>
    </div>
  </div>
</div>
</div>
</div>
{% endfor %}