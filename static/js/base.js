$(document).ready(function() {
    // SideNav Button Initialization
    $(".button-collapse").sideNav2();
    // SideNav Scrollbar Initialization
    var sideNavScrollbar = document.querySelector('.custom-scrollbar');
    var ps = new PerfectScrollbar(sideNavScrollbar);
    //Activate Toast Messages
    $('.toast').toast('show');
    //Detect client time zone
    const timeZoneName = Intl.DateTimeFormat().resolvedOptions().timeZone;
    document.cookie = 'timezone=' + encodeURIComponent(timeZoneName) + '; path=/';
    // Sticky sidebar from MD Bootstrap
    $(function () {
        $(".sticky").sticky({
            topSpacing: 128,
            stopper: "#footer"
        });
    });
});