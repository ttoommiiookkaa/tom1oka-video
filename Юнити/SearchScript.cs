using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class SearchScript : MonoBehaviour
{
    public GameObject ContentHolder;

    public GameObject[] Element;

    public GameObject SearchBar;

    public int totalElements;

    void Start()
    {
        totalElements = ContentHolder.transform.childCount;

        Element = new GameObject[totalElements];

        for (int i = 0; i < totalElements; i++)
        {
            Element[i] = ContentHolder.transform.GetChild(i).gameObject;
        }
    }

    public void Search()
    {
        string SearchText = SearchBar.GetComponent<TMP_InputField>().text;
        int searchTxtlenght = SearchText.Length;

        int searchedElement = 0;

        foreach(GameObject ele in Element)
        {
            searchedElement += 1;

            if(ele.transform.GetChild(0).GetComponent<TextMeshProUGUI>().text.Length >= searchTxtlenght)
            {
                if(SearchText.ToLower() == ele.transform.GetChild(0).GetComponent<TextMeshProUGUI>().text.Substring(0,searchTxtlenght).ToLower())
                {
                    ele.SetActive(true);
                }
                else
                {
                ele.SetActive(false);
                }
            }
        }
    }
}
