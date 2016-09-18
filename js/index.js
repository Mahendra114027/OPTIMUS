$('.control').click( function(){
  $('body').addClass('mode-search');
  $('.input-search').focus();
});

$('.icon-close').click( function(){
  $('body').removeClass('mode-search');
});

var wavesurfer = WaveSurfer.create({
    container: '#waveform',
    waveColor: 'violet',
    progressColor: 'purple'
});
wavesurfer.load('output.wav');