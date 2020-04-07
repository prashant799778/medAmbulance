package com.example.respondermedambulance.Activity;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.util.Log;

import com.example.respondermedambulance.Adapters.Request_Adapter;
import com.example.respondermedambulance.Model.Request;
import com.example.respondermedambulance.R;

import java.util.ArrayList;

public class AllRequestActivity extends AppCompatActivity {
     private RecyclerView recyclerView;
     private ArrayList<Request> requests;
     private   Request_Adapter request_adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_all_request);

        recyclerView=findViewById(R.id.rc_view);
        LinearLayoutManager   manager=new LinearLayoutManager(AllRequestActivity.this);
         recyclerView.setLayoutManager(manager);
        requests=new ArrayList<>();
        requests.add(new Request());
        requests.add(new Request());
        requests.add(new Request());

       request_adapter=new Request_Adapter(requests,getApplicationContext());

    recyclerView.setAdapter(request_adapter);


    }
}
