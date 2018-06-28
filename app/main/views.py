from flask import render_template, request, redirect, url_for, abort
from ..models import User, Promotion, Pick, Production, Interview, CommentsPromotion, CommentsPick, CommentsProduction, \
@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
