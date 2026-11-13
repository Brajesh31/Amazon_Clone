# Asset Inventory

## Summary

The current HTML contains **47 references across 31 unique local image paths** under `imgs/`. The current Git tree does not contain an `imgs/` directory, so none of these relative image paths can resolve in a clean checkout.

Do not download or recreate files based only on Amazon-style filenames. Many filenames appear to be retailer product or promotional assets and may be protected. Add replacements only when their licensing or permission is clear.

## Referenced files

### Category and promotional cards

- `imgs/GirlWatches_1x._SY116_CB564394432_.jpg`
- `imgs/Handbags_1x._SY116_CB566100767_.jpg`
- `imgs/Headphone_1x._SY116_CB566164844_.jpg`
- `imgs/RideOn._SY116_CB545223412_.jpg`
- `imgs/Beauty_1X._SY116_CB563194051_.jpg`
- `imgs/CE24_SUM_GW_DQC_NW_GamingWeek_PC_v2_1x._SY116_CB558844445_.jpg`
- `imgs/Fuji_BTF_Quad_Cards_1x_Pretend_Play_Toys._SY116_CB558654384_.jpg`
- `imgs/Nail_1x._SY116_CB563150139_.jpg`
- `imgs/CleaningTool_2x._SY232_CB563137408_.jpg`
- `imgs/Fuji_Quad_Chair_2x._SY232_CB667159060_.jpg`
- `imgs/Fuji_BTF_Quad_Cards_1x_Desktops._SY116_CB558654384_.jpg`

### Product rail and price-card images

- `imgs/61TVMGeqXGL._AC_SY200_.jpg`
- `imgs/81RnmZtQIJL._AC_SY200_.jpg`
- `imgs/81htrUs4mwL._AC_SY200_.jpg`
- `imgs/81HGALPLEZL._AC_SY200_.jpg`
- `imgs/81qJWNSUpSL._AC_SY200_.jpg`
- `imgs/81CGKCHLbML._AC_SY200_.jpg`
- `imgs/71W5GcQ8-JL._AC_SY200_.jpg`
- `imgs/71ok+FA6jWL._AC_SY200_.jpg`
- `imgs/61kCPwWtBrL._AC_SY200_.jpg`
- `imgs/61iaO-kcHDL._AC_SY200_.jpg`
- `imgs/814T55qCv4L._AC_SY200_.jpg`
- `imgs/71DxWxvCwlL._AC_SY200_.jpg`
- `imgs/71Qa99mgPPL._AC_SY200_.jpg`
- `imgs/71wpE+ZIehL._AC_SY200_.jpg`
- `imgs/71wm42EtoNL._AC_SY200_.jpg`
- `imgs/81X6wvwKSQL._AC_SY200_.jpg`
- `imgs/81sQE5M5HhL._AC_SY200_.jpg`
- `imgs/9171uzu8PEL._AC_SY200_.jpg`
- `imgs/Fragrance_1x._SY116_CB563150139_.jpg`
- `imgs/710yBz6hfUL._AC_SY200_.jpg`

Some paths are referenced more than once in the markup. The unique list above is the set of distinct names seen in the page source.

## Remote resources

The page also uses third-party URLs for the hero carousel, fonts, icons, logo, and small interface icons. These resources are not versioned in the repository and can change or become unavailable independently.

## Recommended resolution

1. Determine which visual assets are actually needed.
2. Source original or permissively licensed alternatives.
3. Record the source and licence for each supplied asset.
4. Store approved files under a consistent local directory.
5. Update the HTML and this inventory.
6. Run `python scripts/check_html.py` and visually review the page.
