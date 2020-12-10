/*
 * Bevragen Ingeschreven Personen
 * API voor het bevragen van ingeschreven personen uit de basisregistratie personen (BRP), inclusief de registratie niet-ingezeten (RNI). Met deze API kun je personen zoeken en actuele gegevens over personen, kinderen, partners en ouders raadplegen.  Gegevens die er niet zijn of niet actueel zijn krijg je niet terug. Heeft een persoon bijvoorbeeld geen geldige nationaliteit, en alleen een beëindigd partnerschap, dan krijg je geen gegevens over nationaliteit en partner.  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-bevragen/tree/v1.1.0/features) voor nadere toelichting. 
 *
 * The version of the OpenAPI document: 1.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * De Link Object zoals gespecificeerd in https://tools.ietf.org/html/draft-kelly-json-hal-08#section-5; Deze link kan als templated link worden aangeboden. [URI-templating is hier beschreven](https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/uri-templating.feature).
 */
@ApiModel(description = "De Link Object zoals gespecificeerd in https://tools.ietf.org/html/draft-kelly-json-hal-08#section-5; Deze link kan als templated link worden aangeboden. [URI-templating is hier beschreven](https://github.com/VNG-Realisatie/Haal-Centraal-common/blob/v1.2.0/features/uri-templating.feature).")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-12-10T12:52:01.057Z[Etc/UTC]")
public class HalLink {
  public static final String SERIALIZED_NAME_HREF = "href";
  @SerializedName(SERIALIZED_NAME_HREF)
  private String href;

  public static final String SERIALIZED_NAME_TEMPLATED = "templated";
  @SerializedName(SERIALIZED_NAME_TEMPLATED)
  private Boolean templated;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;


  public HalLink href(String href) {
    
    this.href = href;
    return this;
  }

   /**
   * Get href
   * @return href
  **/
  @ApiModelProperty(example = "https://datapunt.voorbeeldgemeente.nl/api/v{major-versie}/resourcename/{resource-identificatie}", required = true, value = "")

  public String getHref() {
    return href;
  }


  public void setHref(String href) {
    this.href = href;
  }


  public HalLink templated(Boolean templated) {
    
    this.templated = templated;
    return this;
  }

   /**
   * Get templated
   * @return templated
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getTemplated() {
    return templated;
  }


  public void setTemplated(Boolean templated) {
    this.templated = templated;
  }


  public HalLink title(String title) {
    
    this.title = title;
    return this;
  }

   /**
   * Voor mens leesbaar label bij de link
   * @return title
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "Voor mens leesbaar label bij de link")

  public String getTitle() {
    return title;
  }


  public void setTitle(String title) {
    this.title = title;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HalLink halLink = (HalLink) o;
    return Objects.equals(this.href, halLink.href) &&
        Objects.equals(this.templated, halLink.templated) &&
        Objects.equals(this.title, halLink.title);
  }

  @Override
  public int hashCode() {
    return Objects.hash(href, templated, title);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HalLink {\n");
    sb.append("    href: ").append(toIndentedString(href)).append("\n");
    sb.append("    templated: ").append(toIndentedString(templated)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

