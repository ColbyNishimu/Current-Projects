package com.example.colby.overwatchstats;

import android.content.Intent;
import android.content.res.Resources;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioButton;

import org.xml.sax.InputSource;
import org.xml.sax.XMLReader;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

//Uses Unofficial Overwatch API ver 1.2.0.1b
class getDataTask extends AsyncTask<URL, Void, String> {
    @Override
    protected String doInBackground(URL... url){
        System.out.println("getting data");
        String result = "";
        try(BufferedReader reader = new BufferedReader(new InputStreamReader(url.openStream(), "UTF-8"))){
            for (String line; (line= reader.readLine()) != null;){
                result = result + line;
            }
        }catch(java.io.IOException | Resources.NotFoundException e){
            e.printStackTrace();
        }
        return result;
    }

    protected void onPostExecute(String result){

    }
}

public class login_activity extends AppCompatActivity {

    public final static String EXTRA_MESSAGE = "com.example.colby.overwatchstats.MESSAGE";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login_activity);
    }

    private void getData(String link) throws Resources.NotFoundException, java.io.IOException{
        URL url = null;
        try {
            url = new URL(link);
        } catch (MalformedURLException e) {
            //This is our fault
            System.out.println("Malformed URL");
            e.printStackTrace();
        }
        new getDataTask().execute(url);
    }
    public void onRadioButtonClicked(View view){
        boolean checked = ((RadioButton) view).isChecked();
        switch(view.getId()){
            //If its been checked, do nothing
            case R.id.radio_us:
                if(checked)
                    break;
            case R.id.radio_eu:
                if(checked)
                    break;
            case R.id.radio_kr:
                if(checked)
                    break;
            case R.id.radio_cn:
                if(checked)
                    break;
            case R.id.radio_global:
                if(checked)
                    break;
        }
    }

    public void send_message(View view){
        EditText editText = (EditText) findViewById(R.id.input);
        String message = editText.getText().toString();
        //swtiches # to - in order for the api to work properly
        message = message.replace("#", "-");
        String link = "https://api.lootbox.eu/pc/us/"+message+"/profile";
        try{
            getData(link);
        }catch(Resources.NotFoundException e){
            //Alert box and refresh
            Intent intent = getIntent();
            finish();
            startActivity(intent);
        }catch(java.io.IOException e){
            //This Shouldn't happen in normal circumstances
            System.out.println("IO Exception");
            e.printStackTrace();
        }
        Intent intent = new Intent(this, DisplayStats.class);
        intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);
    }
}
