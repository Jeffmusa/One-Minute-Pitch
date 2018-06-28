from flask import render_template, request, redirect, url_for, abort
from sqlalchemy import func

from . import main
from ..models import User, Promotion, Pick, Production, Interview, CommentsPromotion, CommentsPick, CommentsProduction, \
    CommentsInterview, Like, Unlike
from .forms import UpdateProfile, PromotionForm, PickForm, ProductionForm, InterviewForm, PromotionCommentForm, \
    PickCommentForm, ProductionCommentForm, InterviewCommentForm
from flask_login import login_required, current_user

from .. import db, photos
@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    title = 'Home'

    return render_template('index.html', title=title)

