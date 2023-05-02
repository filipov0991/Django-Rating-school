$(function() {
    var r = $('input[type="range"]');
    r.on('mouseenter', function() {
      var p = r.val();
      r.on('click', function() {
        p = r.val();
        bg(p);
      });
      r.on('mousemove', function() {
        p = r.val();
        bg(p);
      });
    });
  
    function bg(n) {
      r.css({
        'background-image': '-webkit-linear-gradient(left ,#ceb8ee 0%,#8a86c3 ' + n + '%,#e8e8e8 ' + n + '%, #e8e8e8 100%)'
      });
    }
  });