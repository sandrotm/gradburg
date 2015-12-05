var preloadimages = new Array();
function preload(urls) {
    for (i = 0; i < urls.length; i++) {
        preloadimages[i] = new Image();
        preloadimages[i].src = urls[i];
    }
}