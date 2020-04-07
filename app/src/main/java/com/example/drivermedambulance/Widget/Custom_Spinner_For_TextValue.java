package com.example.drivermedambulance.Widget;

import android.content.Context;
import android.util.AttributeSet;
import android.view.View;
import android.view.WindowManager;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.PopupWindow;
import android.widget.TextView;

import androidx.appcompat.widget.AppCompatTextView;

import com.example.drivermedambulance.Comman.Utility;
import com.example.drivermedambulance.R;

import java.util.ArrayList;

public class Custom_Spinner_For_TextValue extends AppCompatTextView implements View.OnClickListener {

    private ArrayList<String> options = new ArrayList<>();
    TextView textView;
    String string="";
    Custom_Spinner_For_TextValue custom_spinner;
    public static String personalTypeValu="";

    public Custom_Spinner_For_TextValue(Context context) {
        super(context);
        initView();
    }

    public Custom_Spinner_For_TextValue(Context context, AttributeSet attrs) {
        super(context, attrs);
        initView();
    }

    public Custom_Spinner_For_TextValue(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        initView();
    }

    private void initView() {
        this.setOnClickListener(this);
    }

    private PopupWindow popupWindowsort(Context context) {

        // initialize a pop up window type
        final TextView textView=this;
        final PopupWindow popupWindow = new PopupWindow(context);
        popupWindow.setWidth(this.getWidth());
        ArrayAdapter<String> adapter = new ArrayAdapter<String>(context,R.layout.spinner_layout,options);
        ListView listViewSort = new ListView(context);
        listViewSort.setDividerHeight(0);
        // set our adapter and pass our pop up window contents
        listViewSort.setAdapter(adapter);

        // set on item selected
        listViewSort.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                popupWindow.dismiss();
                Utility.log("selectedValue---"+position,"--"+options.get(position));
                string=options.get(position);
                custom_spinner.setTag(String.valueOf(options.get(position)));
                textView.setText(string);
//                setText((Integer) parent.getSelectedItem());
            }
        });
//        this.setText(string);

        // some other visual settings for popup window
        popupWindow.setFocusable(true);
         popupWindow.setBackgroundDrawable(getResources().getDrawable(R.color.white));
        popupWindow.setHeight(WindowManager.LayoutParams.WRAP_CONTENT);

        // set the listview as popup content
        popupWindow.setContentView(listViewSort);
        return popupWindow;
    }

    @Override
    public void onClick(View v) {
        if (v == this) {
            PopupWindow window = popupWindowsort(v.getContext());
            window.showAsDropDown(v, 0, 0);
        }
    }

    public void setOptions(ArrayList<String> options, Custom_Spinner_For_TextValue textView) {
        this.options = options;
        this.custom_spinner=textView;
    }
}