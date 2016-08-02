package colby.tipcalculator;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;


public class input extends AppCompatActivity {
    public final static String EXTRA_MESSAGE = "colby.tipcalculator.MESSAGE";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_input);
    }
    public void send_message(View view){
        Intent intent = new Intent(this, CalculateActivity.class);
        EditText editText = (EditText)findViewById(R.id.edit_message);
        String message = editText.getText().toString();
        if (message.matches("[0-9]+([,.][0-9]{1,2})?")) {
            message = message.replace(",", ".");
            intent.putExtra(EXTRA_MESSAGE, message);
            startActivity(intent);
        }
        else{
            editText.setError("Invalid price");
            }
        }
    }

