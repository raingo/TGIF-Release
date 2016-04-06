
/**
 * @overview
 *
 * @author Yuncheng Li (raingomm[AT]gmail.com)
 * @version 2015/08/05
 */

// disable input box before everything else, idealy, this should be on the html, however, not possible with cml:text
Array.each($$('input[type=text]'), function (el) {
    el.set('placeholder', 'Waiting image to load');
    el.set('disabled', 'disabled');
});

requirejs( [
    'https://cdn.rawgit.com/raingo/imagesloaded/master/imagesloaded.pkgd.min.js',
], function( imagesLoaded ) {

    var main = function() {

        //(function(){  'use strict';
        document.onselectstart = function () {
            return false;
        };

        // https://stereochro.me/ideas/detecting-broken-images-js
        function isImageOk(img) {
            // During the onload event, IE correctly identifies any images that
            // weren’t downloaded as not complete. Others should too. Gecko-based
            // browsers act like NS4 in that they report this incorrectly.
            if (!img.complete) {
                return false;
            }

            // However, they do have two very useful properties: naturalWidth and
            // naturalHeight. These give the true size of the image. If it failed
            // to load, either of these should be zero.

            if (typeof img.naturalWidth !== "undefined" && img.naturalWidth === 0) {
                return false;
            }

            // No other way of checking: assume it’s ok.
            return true;
        }

        // This block if/else block is used to hijack the functionality of an existing validator (specifically: yext_no_international_url)
        if (!_cf_cml.digging_gold) {
            CMLFormValidator.addAllThese([
                ['yext_no_international_url', {
                errorMessage: function (el) {

                    if (el.retrieve('detail')) {
                        var error = new Element("div", {
                            'class': "loading_animation",
                        });
                        var err_msg = new Element("pre", {
                            text: el.retrieve('detail')
                        });
                        error.adopt(err_msg);
                        error.inject(el, "after");
                    }

                    return el.retrieve('msg');
                },
                validate: function (el) {
                    var valid = false;

                    try {

                        var clear_detail = function(element) {
                            if (element.getNext() && element.getNext().hasClass("loading_animation")) {
                                element.getNext().destroy();
                            }
                        };

                        var check_img = function(element) {
                            var img_status = element.retrieve('img_status');

                            if (!img_status) {
                                element.store('msg', 'The animated GIF failed to load or is still loading. Please refresh the page or upgrade your browser.');
                                return false;
                            } else {
                                return true;
                            }
                        };

                        var check_new = function(element) {
                            var val = element.get('value');
                            var prev = element.retrieve('prev');
                            if (prev !== null && prev != val) {
                                if (element.retrieve('REQ')) {
                                    element.retrieve('REQ').cancel();
                                }
                                element.store('msg', null);
                                element.store('ajax', null);
                                element.store('REQ', null);
                            }
                            element.store('prev', val);

                        };

                        var validate_text = function(element) {
                            var value = el.get('value');
                            var img_url = el.retrieve('url');
                            var res = false;
                            element.store('msg', 'validating');
                            element.store('ajax', 'waiting');
                            element.store('detail', null);

                            var validator = element.getParentForm().retrieve("validator");
                            var fake_event = {
                                type: "blur"
                            };
                            var boundValidate = validator.validateField.pass([fake_event, element], validator);

                            var handle_ioe = function() {
                                element.store('ajax', 'failed');
                                element.store('msg', 'Please check the network connection and try again.');
                                element.store('prev', '_MAGIC_CLEAN_');
                                boundValidate();
                            };

                            var url = "https://www.cs.rochester.edu/u/yli/lm1.py";
                            var req = new Request.JSONP({
                                url: url,
                                callbackKey: 'callback',
                                timeout: 20000,
                                data: {
                                    q: value,
                                    url: img_url
                                },
                                onComplete: function(response) {
                                    var res = response.status;
                                    element.store('ajax', 'success');
                                    element.store('msg', 'validation failed');
                                    element.store('detail', res);
                                    element.retrieve('hid').set('value', response.gold);
                                    boundValidate();
                                },
                                onTimeout: handle_ioe,
                                onError: handle_ioe,
                                onFailure: handle_ioe
                            });
                            req.send();

                            element.store('REQ', req);
                            return res;
                        };
                        clear_detail(el);
                        if (!check_img(el)) {
                            return false;
                        }
                        el.trim();
                        check_new(el);

                        var ajax = el.retrieve('ajax');
                        if (ajax) {
                            if (ajax == 'success' && !el.retrieve('detail')) {
                                valid = true;
                            }
                        } else {
                            validate_text(el);
                        }
                    } catch (err) {
                        el.store('msg', 'Rare internal errors happened. Please upgrade your browser. Latest Chrome/Firefox/IE should work well.');
                    }
                    return valid;
                }
            }]
            ]);
        } else {
            CMLFormValidator.addAllThese([
                ['yext_no_international_url', {
                validate: function(element, props) {
                    return true;
                }
            }]
            ]);
        }

        function enable_text(el) {
            var cml = $(el.elements[0]);
            var img = cml.getElements('img')[0];
            var hids = cml.getElements('input[type=hidden]');
            var input = cml.getElements('input[type=text]')[0];

            input.store('hid', hids[0]);
            var img_status = isImageOk(img);
            input.store('img_status', img_status);
            input.store('url', img.get('src'));
            input.set('disabled', '');
            input.set('placeholder', 'Please start type the sentence ...');
        }


        Array.each($$('div.cml'), function(el) {
            imagesLoaded(el, enable_text);
        });

        Object.append(Element.NativeEvents, {
            paste: 2,
            drop: 2,
            dragenter: 2,
            dragover: 2
        });

        $$('input').addEvents({
            paste: function (event) {
                event.preventDefault();
            },
            drop: function (event) {
                event.preventDefault();
            },
            dragenter: function(event) {
                event.preventDefault();
            },
            dragover: function(event) {
                event.preventDefault();
            }
        });
    };
    //setTimeout(main, 5000);
    main();
});
