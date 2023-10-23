

$(document).ready(function() {
    // Define a function to fetch and display the common data
    function fetchCommonData() {
        $.ajax({
            url: '/get-common-data/', // Replace with the actual URL of your Django view
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                // console.log(data)
                if ('error' in data) {
                    console.error(data.error);
                } else {

                    var topFooterData = data.top_footer_data;
                    if (topFooterData) {
                        // Clear the existing content inside .f-company
                        $('.f-company').empty();

                        for (var i = 0; i < topFooterData.length; i++) {
                            var heading = topFooterData[i];
                            var contentItems = heading.content_items;

                            var headingHtml = '<div class="f-company">';
                            headingHtml += '<h4>' + heading.heading + '</h4><ul>';

                            for (var j = 0; j < contentItems.length; j++) {
                                var contentItem = contentItems[j];
                                headingHtml += '<li><a href="' + contentItem.url + '">' + contentItem.content + '</a></li>';
                            }

                            headingHtml += '</ul></div>';

                            // Prepend the content for the current heading to .f-company
                            // Prepend makes it get creatreed at the first of all contents in the .top-footer
                            $('.top-footer').prepend(headingHtml);
                        }
                    }

                    if (data.contact_info) {
                        $('#f-contact h4').text('Contact');
                        $('#f-contact ul').html(
                            '<li>' + data.contact_info.address + '</li>' +
                            '<li>' + data.contact_info.email + '</li>' +
                            '<li>' + data.contact_info.phone_number + '</li>'
                        );
                        if (data.contact_info.whatsapp_url) {
                            // Update the href of the #whatsapp-url link
                            $('#whatsapp-url').attr('href', data.contact_info.whatsapp_url);
                        }
                    }
                    if (data.social_media_links) {
                        $('#f-socialmedia h4').text('Social Media');
                    
                        const socialMediaLinks = data.social_media_links;
                    
                        const $ul = $('#f-socialmedia ul');
                        $ul.empty(); // Clear the existing list items
                    
                        // Create and append list items for each social media link that is not empty
                        $.each(socialMediaLinks, function (platform, link) {
                            if (link) { //check list is not empty, then procceed
                                const $li = $('<li></li>');
                                const $a = $('<a></a>', {
                                    href: link,
                                    style: "font-size: 14px"
                                });
                                const $icon = $('<i></i>', {
                                    class: "fa-brands " + "fa-" + platform,
                                    style: "font-size: 20px"
                                });
                    
                                $a.append($icon);
                                $li.append($a);
                                $ul.append($li);
                            }
                        });
                    }
                    
                    // Display base_data information
                    if (data.base_data) {
                        // Display logo image
                        var logoImageUrl = data.base_data.logo_img;
                        $('#logo span.logo img').attr('src', logoImageUrl);

                        // Display logo name
                        var logoName = data.base_data.logo_name;
                        $('#logo span.logo img').attr('alt', logoName);

                        // Display footer
                        var footerText = data.base_data.footer;
                        $('.footer').text('Copyright © ' + footerText);
                    }
                }
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error("Error fetching data: " + errorThrown);
            }
        });
    }

    // Call the fetchCommonData function when the page loads
    fetchCommonData();
});
