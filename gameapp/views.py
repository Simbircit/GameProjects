from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth import logout


def main(request):

    games = GamePage.objects.all()
    genres = Genre.objects.all()

    context = {'games': games, 'genres': genres}
    return render(request, 'gameapp/main.html', context)


def main_genre(request, genre_name):

    games = GamePage.objects.filter(genre__name=genre_name)
    genres = Genre.objects.all()

    context = {'games': games, 'genres': genres}
    return render(request, 'gameapp/main.html', context)


def game_page(request, game_id):

    comments = Comment.objects.filter(game__id=game_id)
    genres = Genre.objects.filter(gamepage=game_id)

    game_obj = get_object_or_404(GamePage, id=game_id)
    game_files = GameFile.objects.filter(game__id=game_id)
    game_img = GamePhoto.objects.filter(game__id=game_id)

    if request.method == 'POST':
        images_form = AddImageForm(request.POST, request.FILES)
        files_form = AddFileForm(request.POST, request.FILES)
        comments_form = CommentForm(request.POST, request.FILES)
        image = GamePhoto()
        file = GameFile()
        comment = Comment()
        if images_form.is_valid():

            image.image = request.FILES.get('image')
            image.game = GamePage.objects.get(id=game_id)
            image.save()

            return redirect(game_page, game_id)

        if files_form.is_valid():

            file.file = request.FILES.get('file')
            file.game = GamePage.objects.get(id=game_id)
            file.save()

            return redirect(game_page, game_id)

        if comments_form.is_valid():

            comment.user = User.objects.get(username=request.user.username)
            comment.game = GamePage.objects.get(id=game_id)
            comment.text = request.POST.get('text')
            comment.save()

            return redirect(game_page, game_id)

    else:

        images_form = AddImageForm
        files_form = AddFileForm
        comments_form = CommentForm

    context = {'game': game_obj, 'game_files': game_files, 'game_img': game_img, 'comments': comments, 'genres': genres,
               'images_form': images_form, 'files_form': files_form, 'comments_form': comments_form}

    return render(request, 'gameapp/game.html', context)


def add_game(request):

    genres = Genre.objects.all()

    if request.method == 'POST':

        form = GameForm(request.POST, request.FILES)
        game = GamePage()
        game.user = User.objects.get(username=request.user.username)
        game.name = request.POST.get('name')
        game.description = request.POST.get('description')
        game.image = request.FILES.get('image')
        genre_ids = request.POST.getlist('genre')
        game.save()
        genres = Genre.objects.filter(id__in=genre_ids)
        game.genre.set(genres)

        return HttpResponseRedirect(f'/game/{game.id}')

    else:

        form = GameForm

        return render(request, 'gameapp/add_game.html', {'form': form})


def delete_image(request, image_id):

    image = GamePhoto.objects.get(id=image_id)
    image.delete()

    return redirect(game_page, image.game.id)


def delete_file(request, file_id):

    file = GameFile.objects.get(id=file_id)
    file.delete()

    return redirect(game_page, file.game.id)


def register(request):

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:

        form = CreateUser

    return render(request, 'gameapp/register.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'gameapp/profile.html', context)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
