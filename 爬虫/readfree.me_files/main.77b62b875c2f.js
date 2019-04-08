//btn js
function update_limit(css,title,left){
    var self = $('#id_limit');
    if (self.length){
        self.attr('class',css).attr('title',title).text(left);
    };
};

function disable_take(){
    var objs = $('.book-down, .book-push');
    if (objs.length){
        objs.attr('disabled','disabled');
        objs.attr('title','今日余额已用完');
    };
};

function on_book_push_click(){
    var self = $(this);
    var pk = $(this).data('pk');
    var pushmail = $(this).data('pushmail');
    var args = {pk: pk, pushmail: pushmail};
    var args = {
        pk: pk,
        pushmail: pushmail,
    };
    $.get(g_url_push, args, function(data){
        if (data.ret == 'ok') {
            if (self.is('button')) {
                self.find('span').text(data.count);
                self.addClass('btn-inverse').removeClass('btn-success');
                self.next('.dropdown-toggle').addClass('btn-inverse').removeClass('btn-success');
            } else {
                self.addClass('pushmail-inverse');
                self.parents('.btn-group').children('button').addClass('btn-inverse').removeClass('btn-success').find('.push-num').text(data.count);
            }
            update_limit(data.css,data.title,data.left);
            if (data.left < 1){
                disable_take();
            }
            pop_info(data.msg);
        } else {
            pop_error(data.msg);
        }
    })
}

function on_book_wish_click(){
    var self = $(this);
    var pk = self.closest('li').attr('pk');
    var args = {pk:pk};
    $.get(g_url_wish,args,function(data){
        var ret = data.ret;
        if (ret == 'ok') {
            self.toggleClass('btn-inverse').toggleClass('btn-success');
            self.find('span').text(data.count);
        } else {
            pop_info(ret);
        }
    })
}

function on_book_down_click(){
    var self = $(this);
    var title = self.attr('title');
    var parent = self.closest('li');
    var count = self.find('span').text();
    if (count != '1k+') {
        var x = parseInt(count) + 1;
        self.find('span').text(x);
    }
    self.addClass('btn-inverse').removeClass('btn-success');
    var limit_obj = $('#id_limit');
    if (limit_obj.length > 0){
        var left = parseInt(limit_obj.text());
        if (left > 0){
            left -= 1;
            limit_obj.text(left);
        };
        if (left < 3){
            limit_obj.css('badge badge-important');
        };
        if (left < 1){
            disable_take();
        };
    };
}

function bind_btn_click(){
    $(document).on('click', '.book-push', on_book_push_click);
    $(document).on('click', '.book-down', on_book_down_click);
    $(document).on('click', '.book-wish', on_book_wish_click);
}

bind_btn_click();


//lightbox
function lightbox_close(e) {
    $('body').removeClass('noscroll');
    $('#lightbox').hide();
    $('#pjax').html('');
    history.pushState({},'',g_url_back);
};

$('#lightbox').click(function(e){
    if (e.target == this){
        lightbox_close(e);
    }
});

$(document).keyup(function(e) {
    if (e.keyCode == 27) {
        lightbox_close(e);
    }
});

//alerts
var delayTime  = 5000;
var alerts     = $('.messages.alert');

delayTime = delayTime + (alerts.length * 250);

alerts.each(function() {
    $(this).delay(delayTime).fadeOut('slow');
    delayTime -= 250;
});

//chosen
$('form.chosen select').chosen();

//popover
$('.pop-over').popover({
    placement: function(tip, element) {
            var offset = $(element).offset();
            height = $(document).outerHeight();
            width = $(document).outerWidth();
            vert = 0.5 * height - offset.top;
            vertPlacement = vert > 0 ? 'bottom' : 'top';
            horiz = 0.5 * width - offset.left;
            horizPlacement = horiz > 0 ? 'right' : 'left';
            placement = Math.abs(horiz) > Math.abs(vert) ?  horizPlacement : vertPlacement;
            return placement;
        }
});

$('.pop-over').click(function(e){
    $(this).popover('hide');
});

//message
Messenger.options = {
    extraClasses: 'messenger-fixed messenger-on-bottom messenger-on-right',
    theme: 'future',
};
function pop_msg(type,msg) {
    Messenger().post({
      message: msg,
      type: type,
      showCloseButton: true,
    });
};
function pop_info(msg) {pop_msg('info',msg)};
function pop_error(msg) {pop_msg('error',msg)};
function pop_success(msg) {pop_msg('success',msg)};

$('.z-link-search').click(function(){
    ga('send', 'event', 'link', 'click', 'z-link-search');
});

$('.z-link-product').click(function(){
    ga('send', 'event', 'link', 'click', 'z-link-product');
});

//pjax
$.pjax.defaults.scrollTo = false;

$(document).pjax('a.pjax', '#pjax');

$(document).on('pjax:beforeSend', function() {
    $('body').addClass('noscroll');
    $('#lightbox').show();
});

$(document).on('pjax:send', function() {
    $('.loading-container').show();
});

$(document).on('pjax:complete', function() {
    $('.loading-container').hide();
    $('#pjax-close').click(lightbox_close);
});

$(document).on('pjax:timeout', function(e) {
    e.preventDefault();
    return false;
});

$(document).on('pjax:error', function(e) {
    e.preventDefault();
    return false;
});

