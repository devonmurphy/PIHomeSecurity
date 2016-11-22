<!DOCTYPE HTML>  
<html>
<body> 

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<button id="start">Start Stream</button>
<button id="stop">Stop Stream</button>
<p></p>
<script type="text/javascript">
     function sleep(delay) {
        var start = new Date().getTime();
        while (new Date().getTime() < start + delay);
      }
   $(document).ready(function(){
	$("#start").click(function(){
            $.ajax({
                type: 'POST',
                url: '/',
				data: 'start',
                success: function(data) {
                }
            });
   });
	$("#stop").click(function(){
            $.ajax({
                type: 'POST',
                url: '/',
				data: 'stop',
                success: function(data) {
                }
            });
   });
});
</script>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Y4pEOiWH0qM" frameborder="0" allowfullscreen></iframe>
</body>
</html>
