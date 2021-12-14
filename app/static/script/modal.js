$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (taskID === 'New Task') {
            modal.find('.input-group-text').text("City Name")
            modal.find('.modal-title').text("Add City")
            $('#task-form-display').removeAttr('taskID')
        } else {
            modal.find('.input-group-text').text("Population")
            modal.find('.modal-title').text('Edit Population')
            $('#task-form-display').attr('taskID', taskID)
        }

        if (content) {
            modal.find('.form-control').val(content);
        } else {
            modal.find('.form-control').val('');
        }
    })


    $('#submit-task').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#task-modal').find('.form-control').val()
            }),
            success: function (res) {
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });


    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                location.reload();
            },
            error: function () {
                alert("Something went wrong")
            }
        });
    });

    $('#search-tropical').click(function() {
        $.ajax({
            type: 'POST',
            url: '/tropical',
            success: function (res) {
                var str = "<tr><th>City</th> <th>Country</th> <th>Population</th><th>Latitute</th><th>Longitude</th></tr>"
                for(var i  = 0; i<res.res.length; i++) {
                    str += "<tr><td>"+res.res[i].city+"</td>  <td>"+res.res[i].country+"</td> <td>"+res.res[i].population+"</td><td>"+res.res[i].latitute+"</td><td>"+res.res[i].longitude+"</td></tr>"
                }
                $("#CITYTABLE").html(str)

            },
            error: function () {
                alert("Something went wrong")
            }
        });
    });

     $('#search-culture').click(function() {
        $.ajax({
            type: 'POST',
            url: '/culture',
            success: function (res) {
                var str = "<tr><th>Country</th> <th>Number of Museums</th></tr>"
                for(var i  = 0; i<res.res.length; i++) {
                    str += "<tr><td>"+res.res[i].country+"</td> <td>"+res.res[i].numberofmuseums+"</td></tr>"
                }
                $("#CITYTABLE").html(str)
            },
            error: function () {
                alert("Something went wrong!")
            }
        });
    })

    $('#search-city').click(function() {
        var val = $("#findcity").val()
        $.ajax({
            type: 'POST',
            url: '/searchcity/'+val,
            success: function (res) {
                var str = "<tr><th>City</th> <th>Country</th> <th>Population</th></tr>"
                str += "<tr><td>"+res.res[0].city+"</td> <td>"+res.res[0].country+"</td> <td>"+res.res[0].population+"</td></tr>"
                $("#CITYTABLE").html(str)
            },
            error: function() {
                alert("Something went wrong")
            }
        })
    });

     $('#search-good-accommodation').click(function() {
        $.ajax({
            type: 'POST',
            url: '/accommodation',
            success: function (res) {
                var str = "<tr><th>City</th> <th>Average Temperature</th> <th>Possibility To Find A Accommodation With Free WIFI</th>" +
                    "<th>Average Rating Of Accommodations</th><th>Ranking Of Accommodations</th></tr>";
                for(var i  = 0; i<res.res.length; i++) {
                    str += "<tr><td>" + res.res[i].city + "</td> <td>" + res.res[i].averageTemperature + "</td> <td>" + res.res[i].possibilityToFindAAccommodationWithFreeWifi + "</td>" +
                        "<td>" + res.res[i].averageRatingOfAccommodations + "</td><td>" + res.res[i].rankingOfaccommodations + "</td></tr>"
                }
                $("#CITYTABLE").html(str)
            },
            error: function() {
                alert("Something went wrong")
            }
        })
    });


    $("#clear-table").click(function(){
        $.ajax({
            type:"POST",
            url:'/clear',
            success: function (res) {
                $("#CITYTABLE").html("")
            },
            error: function () {
                alert("Failed to clean")
            }
        })
    })

});