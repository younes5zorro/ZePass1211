$(function () {
            $("#btn_recd").click(function(){
				$.get("http://127.0.0.1:5000/api/find/"+$('#select_user').val()+"/"+$('#select_model').val(), function (data) {
                    $('.container_id1').fadeOut();
                    $('.container_id1').empty();
                    $(".container_id1").append($("<h1>Recommendation For User </h1>"));
                    $(".container_id1").append($("<div class='fillrec-"+$('#select_user').val()+"' ></div>"));

                    $.each(JSON.parse(data), function (i, item) {
                        
                        $(".fillrec-"+$('#select_user').val()).append($('\
                            <div class="example-2 card">    \
                                    <div class="wrapper" style="background: url(\''+item.data.Poster+'\') center/cover no-repeat;">\
                                        <div class="header">\
                                            <div class="date">\
                                                '+item.data.Released+'\
                                            </div>\
                                            <ul class="menu-content">\
                                                <li><span>'+item.data.imdbRating+'</span></li>\
                                                <li><span class="star">★</span></li>\
                                            </ul>\
                                        </div>\
                                        <div class="data">\
                                            <div class="content">\
                                                <a data-toggle="modal" data-target="#myModalrec-'+item.movie_id+'" class="button">Read more</a>\
                                            </div>\
                                        </div>\
                                    </div>\
                             </div>\
                        '));

                        $(".modals").append('<div class="modal fade" id="myModalrec-'+item.movie_id+'" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"> \
							        <div class="modal-dialog" role="document"> \
									<div class="moviecard">\
									<div class="movie-poster play-trailer" style="background: url(\''+item.data.Poster+'\');background-size: cover;"></div>\
									<div id="movie-content">\
										<div class="movie-ratings"><span class="star">★</span><span class="score">'+item.data.imdbRating+'</span><span class="score-out-of">/ 10 (IMDB)</span></div>\
										<div class="movie-title"><a href="http://www.imdb.com/title/'+item.data.imdbID+'" target="_blank">'+item.data.Title+'</a><span class="movie-year">'+item.data.Year+'</span></div>\
										<div class="movie-details"><span class="movie-rating">R</span><span class="movie-duration">'+item.data.Runtime+'</span><span class="movie-genre">'+item.data.Genre+'</span></div>\
										<div class="movie-castcrew"><span class="title">Director</span><span class="name">'+item.data.Director+'</span></div>\
										<div class="movie-castcrew"><span class="title">Writer</span><span class="name">'+item.data.Writer+'</span></div>\
										<div class="movie-castcrew"><span class="title">Cast</span><span class="name">'+item.data.Actors+'</span></div>\
										<div class="movie-castcrew"><span class="title">Language</span><span class="name">'+item.data.Language+'</span></div>\
										<div class="movie-castcrew"><span class="title">Country</span><span class="name">'+item.data.Country+'</span></div>\
										<div class="movie-synopsis">'+item.data.Plot+'</div>\
									</div>\
									</div>\
							</div>\
                            </div>'
                        )
                       
                    });
                    new FilmRoll({
                        container: ".fillrec-"+$('#select_user').val(),
                        pager:false,
                        configure_load: true,
                    });
                    $('.container_id1').fadeIn("slow")
                })
                

            });
		
            
            $('#select_user').on("change", function () {
                $('.container_id1').empty();
				$.get("http://127.0.0.1:5000/api/movie_user/"+$('#select_user').val(), function (data) {
                    $('.container_id').empty();
                    $(".container_id").append($("<h1>Films Aimer par User </h1>"));
                    $(".container_id").append($("<div class='fill-"+$('#select_user').val()+"' ></div>"));
					$.each(JSON.parse(data), function (i, item) {

                        $(".fill-"+$('#select_user').val()).append($('\
                            <div class="example-2 card">    \
                                    <div class="wrapper" style="background: url(\''+item.data.Poster+'\') center/cover no-repeat;">\
                                        <div class="header">\
                                            <div class="date">\
                                                '+item.data.Released+'\
                                            </div>\
                                            <ul class="menu-content">\
                                                <li><span>'+item.data.imdbRating+'</span></li>\
                                                <li><span class="star">★</span></li>\
                                            </ul>\
                                        </div>\
                                        <div class="data">\
                                            <div class="content">\
                                                <a data-toggle="modal" data-target="#myModal-'+item.movie_id+'" class="button">Read more</a>\
                                            </div>\
                                        </div>\
                                    </div>\
                             </div>\
                        '));
                       

                        $(".modals").append('<div class="modal fade" id="myModal-'+item.movie_id+'" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"> \
							        <div class="modal-dialog" role="document"> \
									<div class="moviecard">\
									<div class="movie-poster play-trailer" style="background: url(\''+item.data.Poster+'\');background-size: cover;"></div>\
									<div id="movie-content">\
										<div class="movie-ratings"><span class="star">★</span><span class="score">'+item.data.imdbRating+'</span><span class="score-out-of">/ 10 (IMDB)</span></div>\
										<div class="movie-title"><a href="http://www.imdb.com/title/'+item.data.imdbID+'" target="_blank">'+item.data.Title+'</a><span class="movie-year">'+item.data.Year+'</span></div>\
										<div class="movie-details"><span class="movie-rating">R</span><span class="movie-duration">'+item.data.Runtime+'</span><span class="movie-genre">'+item.data.Genre+'</span></div>\
										<div class="movie-castcrew"><span class="title">Director</span><span class="name">'+item.data.Director+'</span></div>\
										<div class="movie-castcrew"><span class="title">Writer</span><span class="name">'+item.data.Writer+'</span></div>\
										<div class="movie-castcrew"><span class="title">Cast</span><span class="name">'+item.data.Actors+'</span></div>\
										<div class="movie-castcrew"><span class="title">Language</span><span class="name">'+item.data.Language+'</span></div>\
										<div class="movie-castcrew"><span class="title">Country</span><span class="name">'+item.data.Country+'</span></div>\
										<div class="movie-synopsis">'+item.data.Plot+'</div>\
									</div>\
									</div>\
							</div>\
                            </div>'
                        )
                    });
                    new FilmRoll({
                        container: ".fill-"+$('#select_user').val(),
                        pager:false,
                        configure_load: true,
                    });
                    
                })
               
				// $('#container_id').hide().fadeIn(500)
               
			})
			 
                

           
            $.get("http://127.0.0.1:5000/api/users/30", function (data) {
                $.each(JSON.parse(data), function (i, item) {
                    $('#select_user').append($('<option>', {
                        value: item.user_id,
                        text: item.user_id
                    }));
                });
                $('#select_user').trigger("change")
            })

           
			





});
       