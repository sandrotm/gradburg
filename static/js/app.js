//show active menu item
var url = window.location.href;
var activeItem = $('.menuitem').filter(function () {
    return $(this).find('a')[0].href == url;
});

activeItem.addClass('menuitem-active');

var currentPage = activeItem.size() > 0 ? activeItem.data('page-id') : 'home';



$(document).foundation();


var preloadimages = new Array();
function preload(urls) {
    for (i = 0; i < urls.length; i++) {
        preloadimages[i] = new Image();
        preloadimages[i].src = urls[i];
    }
}




//flats
switch (currentPage) {
    case 'home':
        var position = {lat: 41.7406522, lng: 44.7876616},
            metroPos = {lat: 41.7429269, lng: 44.7839426},
            markerPos = {lat: 41.7382259, lng: 44.7919417},
            directionsDisplay = new google.maps.DirectionsRenderer(),
            directionsService = new google.maps.DirectionsService();

        function initialize() {
            var mapCanvas = document.getElementById('map');

            var mapOptions = {
                center: new google.maps.LatLng(position.lat, position.lng),
                zoom: 15,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            }

            var map = new google.maps.Map(mapCanvas, mapOptions);
            var marker = new google.maps.Marker({
                position: markerPos,
                map: map,
                title: 'Gradburg'
            });

            directionsDisplay.setMap(map);
            calcRoute();

        }

        google.maps.event.addDomListener(window, 'load', initialize);


        function calcRoute() {
            var request = {
                origin:metroPos,
                destination:markerPos,
                travelMode: google.maps.TravelMode.WALKING
            };
            directionsService.route(request, function(result, status) {
                if (status == google.maps.DirectionsStatus.OK) {
                    directionsDisplay.setDirections(result);
                }
            });
        }




        var bg1 = $('#bannerhead1 #bg-wrapper .bg1'),
            bg2 = $('#bannerhead1 #bg-wrapper .bg2');

        var backgrounds = new Array(
                //'url(../../media/images/banners/1.jpg)',
                '../../media/images/banners/2.jpg',
                '../../media/images/banners/3.jpg',
                '../../media/images/banners/4.jpg',
                '../../media/images/banners/5.jpg'
        );
        preload(backgrounds);

        var bgChangeInterval;
        var current = 0, next = 0;
        bg1.css('background-image', 'url(' + backgrounds[1] + ')');
        bg2.css('background-image', 'url(' + backgrounds[0] + ')');
        var bgs = [bg1, bg2];
        var topBg = bg2;
        var lastChangeTime = 0;
        var duration = 10000;
        var elapsed = 0;
        var y = 0, minY = -200, maxY = 0, speed = 0.02, prevTime = Date.now(), deltaTime = 0;

        function nextBackground() {
            current = next;
            next++;
            next = next % backgrounds.length;
            bgs[0].css('opacity', '0.0').css('z-index', 2).css('transform', 'translate3d(0, 0, 0)');
            y = 0;
            topBg = bgs[0];
            bgs[1].css('z-index', '1');

            bgs[0].fadeTo(1500, 1, function () {
                bgs[1].css('background-image', 'url(' + backgrounds[(next + 1) % backgrounds.length] + ')');
                var t = bgs[0];
                bgs[0] = bgs[1];
                bgs[1] = t;
            });
            lastChangeTime = Date.now();
        bgChangeInterval = window.setTimeout(nextBackground, duration);
        }

        var bgChangeInterval;
        function startBgChanger () {
            lastChangeTime = Date.now();
            bgChangeInterval = window.setTimeout(nextBackground, duration - elapsed);
        elapsed = 0;
        prevTime = lastChangeTime;
        }
        function stopBgChanger () {
            window.clearTimeout(bgChangeInterval);
            elapsed = (Date.now() - lastChangeTime);
        }

        window.addEventListener('focus', startBgChanger);
        window.addEventListener('blur', stopBgChanger);

        $(document).ready(function() {
            startBgChanger();
        });



        window.requestAnimationFrame(animate);

        function animate () {
            window.requestAnimationFrame(animate);

            time = Date.now();
            deltaTime = time - prevTime;

            prevTime = time;

            y -= deltaTime * speed;
            if (y <= minY) {
                y = minY;
            }
            topBg[0].style.transform = ['translate3d(0, ' + y +'px, 0)'];
        }
        break;
    case 'flats':
        $(function () {
            var lightbox1 = $('#panel1 div.imgholder a').simpleLightbox({
                close: true,
                overlay: true,
            })
            var lightbox2 = $('#panel2 div.imgholder a').simpleLightbox({
                close: true,
                overlay: true,
            })
            var lightbox3 = $('#panel3 div.imgholder a').simpleLightbox({
                close: true,
                overlay: true,
            })
        })


        var flatImages =
            $('.imgholder img')
                .map(function (elem) {
                    return this.src;
                })
                .get();

        preload(flatImages);
        break;
    case 'process':
        $('#bigimage').attr('src', $('#gallery a').first()[0].href);
        document.getElementById('gallery').onclick = function (event) {
            event = event || window.event;
            var target = event.target || event.srcElement,
                    link = target.src ? target.parentNode : target,
                    options = {index: link, event: event},
                    links = this.getElementsByTagName('a');

            if (link != '[object HTMLDivElement]')
                $('#bigimage').attr('src', link);

            event.preventDefault();
        };
        break;
}