

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
                        $('#f-socialmedia ul li a:nth-child(1)').attr('href', data.social_media_links.facebook_link);
                        $('#f-socialmedia ul li a:nth-child(2)').attr('href', data.social_media_links.twitter_link);
                        $('#f-socialmedia ul li a:nth-child(3)').attr('href', data.social_media_links.whatsapp_link);
                        $('#f-socialmedia ul li a:nth-child(4)').attr('href', data.social_media_links.linkedIn_link);
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
