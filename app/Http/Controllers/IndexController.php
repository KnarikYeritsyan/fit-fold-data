<?php

namespace App\Http\Controllers;

use App\DatabaseJson\Models\View as DBView;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\View;

class IndexController extends Controller
{

    function homePage()
    {
        return view('welcome');
    }

    function papers()
    {
        return view('papers');
    }

    function examples()
    {
        return view('examples');
    }

    function cd_examples()
    {
        return view('cd-examples');
    }

    function cd_fitting()
    {
        return view('cd-fitting');
    }

    function cal_fitting()
    {
        return view('cal-fitting');
    }

    function cal_examples()
    {
        return view('cal-examples');
    }

    public function cal_download($dir,$file){
        return response()->download(storage_path('cal-examples/'.$dir.'/'.$file));
    }

    public function cd_download($method,$dir,$file){
        return response()->download(storage_path('cd-examples/'.$method.'/'.$dir.'/'.$file));
    }
}
