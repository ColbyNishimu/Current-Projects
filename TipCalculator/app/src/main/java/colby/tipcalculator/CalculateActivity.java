package colby.tipcalculator;

import android.annotation.TargetApi;
import android.app.ActionBar;
import android.content.Intent;
import android.icu.text.DecimalFormat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.lang.annotation.Target;

public class CalculateActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calculate);
        Intent intent = getIntent();
        String message = intent.getStringExtra(input.EXTRA_MESSAGE);
        double amount = Double.parseDouble(message);
        double tip = amount*.15;
        String tipamt = getCorrectFormat(tip);
        TextView tipView = (TextView) findViewById(R.id.tipamount);
        tipView.setTextSize(40);
        tipView.setText("Tip Amount: "+tipamt);

        double val = amount+tip;
        String result = getCorrectFormat(val);
        if(result.substring(result.indexOf(".")+1).length() == 1) {
            result = result + "0";
        }
        TextView textView = (TextView)findViewById(R.id.tiptotal);
        textView.setTextSize(40);
        textView.setText("Tip Total: "+result);
    }
    public void send_message(View view){
        Intent intent = new Intent(this, input.class);
        startActivity(intent);
    }

    public String getCorrectFormat(double amount){
        double temp = amount*100;
        double temp1 = Math.round(temp);
        double result = temp1/100;
        return "$"+Double.toString(result);
    }

}
