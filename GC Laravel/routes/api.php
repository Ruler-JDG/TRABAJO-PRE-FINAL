<?php
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\GiftcardController;

Route::apiResource('giftcards', GiftcardController::class);
