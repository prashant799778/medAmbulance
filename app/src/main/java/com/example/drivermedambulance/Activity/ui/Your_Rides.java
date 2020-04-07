package com.example.drivermedambulance.Activity.ui;

import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import com.example.drivermedambulance.Adapters.YourRidePaginationAdapter;
import com.example.drivermedambulance.Adapters.listeners.PaginationListener;
import com.example.drivermedambulance.Api_Calling.MyResult;
import com.example.drivermedambulance.Comman.MySharedPrefrence;
import com.example.drivermedambulance.Model.YourRide;
import com.example.drivermedambulance.R;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

import static com.example.drivermedambulance.Adapters.listeners.PaginationListener.PAGE_START;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link Your_Rides#newInstance} factory method to
 * create an instance of this fragment.
 *
 */
public class Your_Rides extends Fragment implements MyResult, SwipeRefreshLayout.OnRefreshListener {

    MyResult myResult;
    MySharedPrefrence sharedPrefrence;
    RecyclerView listView;
    int limit =0;
    int offset = 10;
    SwipeRefreshLayout swipeRefreshLayout;
    YourRidePaginationAdapter adapter;

    private int currentPage = PAGE_START;
    private boolean isLastPage = false;
    private int totalPage = 10;
    private boolean isLoading = false;
    int itemCount = 0;

    public static Your_Rides newInstance() {
        Your_Rides fragment = new Your_Rides();
        Bundle args = new Bundle();
        fragment.setArguments(args);
        return fragment;
    }
    public Your_Rides() {
        // Required empty public constructor
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_your__rides, container, false);
        this.myResult = this;
        swipeRefreshLayout = (SwipeRefreshLayout) view.findViewById(R.id.swipeRefresh);
        listView = (RecyclerView) view.findViewById(R.id.list_view);
        listView.setHasFixedSize(true);
        LinearLayoutManager layoutManager = new LinearLayoutManager(getContext());
        listView.setLayoutManager(layoutManager);
        List<YourRide> rides = new ArrayList<>();
        rides.add(new YourRide());
        rides.add(new YourRide());

        adapter = new YourRidePaginationAdapter(rides);
        listView.setAdapter(adapter);
        doApiCall();
        sharedPrefrence = MySharedPrefrence.instanceOf(getContext());
        //Api_Calling.postMethodCall(getContext(), URLS.YOUR_RIDE,view,myResult,"YourRide",getRide());

        listView.addOnScrollListener(new PaginationListener(layoutManager) {
            @Override
            protected void loadMoreItems() {
                isLoading = true;
                currentPage++;
                doApiCall();
            }

            @Override
            public boolean isLastPage() {
                return isLastPage;
            }

            @Override
            public boolean isLoading() {
                return isLoading;
            }
        });

        return view;
    }

    @Override
    public void onResult(JSONObject object, Boolean status) {
        if(object==null){
            listView.setVisibility(View.VISIBLE);
            List<YourRide> rides = new ArrayList<>();
            rides.add(new YourRide());
            rides.add(new YourRide());
            rides.add(new YourRide());
            rides.add(new YourRide());
            rides.add(new YourRide());
            Log.d("TAG", "onResult: "+rides.size());
            /*listView.setAdapter(new YourRideListAdapter(rides));
            listView.setLayoutManager(new LinearLayoutManager(getContext()));
            listView.setItemAnimator(new DefaultItemAnimator());*/
        }else{
            // No Data Found
            listView.setVisibility(View.GONE);
        }
    }

    public JSONObject getRide()
    {
        JSONObject jsonObject=new JSONObject();
        try {
            jsonObject.put("startLimit",limit).put("endLimit",offset)
                    .put("userId",sharedPrefrence.getUserId());
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return jsonObject;

    }

    @Override
    public void onRefresh() {
        itemCount = 0;
        currentPage = PAGE_START;
        isLastPage = false;
        adapter.clear();
        doApiCall();
    }

    private void doApiCall() {
        final ArrayList<YourRide> items = new ArrayList<>();
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 10; i++) {
                    itemCount++;
                    YourRide postItem = new YourRide();
                    items.add(postItem);
                }
                /**
                 * manage progress view
                 */
                if (currentPage != PAGE_START) adapter.removeLoading();
                adapter.addItems(items);
                swipeRefreshLayout.setRefreshing(false);
                // check weather is last page or not
                if (currentPage < totalPage) {
                    adapter.addLoading();
                } else {
                    isLastPage = true;
                }
                isLoading = false;
            }
        }, 1500);
    }

}
