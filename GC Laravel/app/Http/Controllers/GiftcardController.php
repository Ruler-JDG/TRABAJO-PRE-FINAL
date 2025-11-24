<?php
namespace App\Http\Controllers;

use App\Models\Giftcard;
use Illuminate\Http\Request;

class GiftcardController extends Controller
{
    // GET all
    public function index() {
        return response()->json(Giftcard::all(), 200);
    }

    // POST create
    public function store(Request $request) {
        $data = $request->validate([
            'code' => 'required|unique:giftcards,code',
            'amount' => 'required|numeric',
            'is_active' => 'boolean'
        ]);

        $gift = Giftcard::create($data);
        return response()->json($gift, 201);
    }

    // GET one
    public function show($id) {
        $gift = Giftcard::findOrFail($id);
        return response()->json($gift, 200);
    }

    // PUT update
    public function update(Request $request, $id) {
        $gift = Giftcard::findOrFail($id);
        $gift->update($request->only(['code','amount','is_active']));
        return response()->json($gift, 200);
    }

    // DELETE
    public function destroy($id) {
        $gift = Giftcard::findOrFail($id);
        $gift->delete();
        return response()->json(['message' => 'Giftcard deleted'], 200);
    }
}
