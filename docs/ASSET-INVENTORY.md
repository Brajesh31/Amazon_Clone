# 🖼️ Asset Inventory and Usage-Rights Register

## 1. Purpose

This inventory records the visual resources referenced by the current HTML. It is also a remediation record for missing local files and an approval checklist for future assets.

A filename or public URL is not evidence of permission to redistribute an image. Do not fetch or repackage retailer assets solely because the page refers to them.

## 2. Current local asset status

The page source contains **47 local image references across 31 unique path names** under `imgs/`. The tracked repository tree does not contain an `imgs/` directory. Consequently, these references cannot resolve in a clean checkout.

The list below is derived from the current `index.html` source and should be regenerated or reviewed whenever image markup changes.

### 2.1 Category and promotional card paths

| Path | Current use | Status |
|---|---|---|
| `imgs/GirlWatches_1x._SY116_CB564394432_.jpg` | First promotional/category card | Missing |
| `imgs/Handbags_1x._SY116_CB566100767_.jpg` | Second promotional/category card | Missing |
| `imgs/Headphone_1x._SY116_CB566164844_.jpg` | Third promotional/category card | Missing |
| `imgs/RideOn._SY116_CB545223412_.jpg` | Fourth promotional/category card | Missing |
| `imgs/Beauty_1X._SY116_CB563194051_.jpg` | Grooming category card | Missing |
| `imgs/CE24_SUM_GW_DQC_NW_GamingWeek_PC_v2_1x._SY116_CB558844445_.jpg` | Devices and laptop category cards | Missing |
| `imgs/Fuji_BTF_Quad_Cards_1x_Pretend_Play_Toys._SY116_CB558654384_.jpg` | Toys category card | Missing |
| `imgs/Nail_1x._SY116_CB563150139_.jpg` | Fashion category card | Missing |
| `imgs/CleaningTool_2x._SY232_CB563137408_.jpg` | Home category card | Missing |
| `imgs/Fuji_Quad_Chair_2x._SY232_CB667159060_.jpg` | Office chair category card | Missing |
| `imgs/Fuji_BTF_Quad_Cards_1x_Desktops._SY116_CB558654384_.jpg` | Gaming monitor category card | Missing |

### 2.2 Product rail and deal card paths

| Path | Current use | Status |
|---|---|---|
| `imgs/61TVMGeqXGL._AC_SY200_.jpg` | Product rail image | Missing |
| `imgs/81RnmZtQIJL._AC_SY200_.jpg` | Product rail image | Missing |
| `imgs/81htrUs4mwL._AC_SY200_.jpg` | Product rail image | Missing |
| `imgs/81HGALPLEZL._AC_SY200_.jpg` | Product rail image | Missing |
| `imgs/81qJWNSUpSL._AC_SY200_.jpg` | Product rail image | Missing |
| `imgs/81CGKCHLbML._AC_SY200_.jpg` | Product rail and deal card image | Missing |
| `imgs/71W5GcQ8-JL._AC_SY200_.jpg` | Product rail image | Missing |
| `imgs/71ok+FA6jWL._AC_SY200_.jpg` | Product rail image | Missing |
| `imgs/61kCPwWtBrL._AC_SY200_.jpg` | Product rail image | Missing |
| `imgs/61iaO-kcHDL._AC_SY200_.jpg` | Product rail image | Missing |
| `imgs/814T55qCv4L._AC_SY200_.jpg` | Deal card image | Missing |
| `imgs/71DxWxvCwlL._AC_SY200_.jpg` | Deal card image | Missing |
| `imgs/71Qa99mgPPL._AC_SY200_.jpg` | Deal card image | Missing |
| `imgs/71wpE+ZIehL._AC_SY200_.jpg` | Deal card image | Missing |
| `imgs/71wm42EtoNL._AC_SY200_.jpg` | Deal card image | Missing |
| `imgs/81X6wvwKSQL._AC_SY200_.jpg` | Deal card image | Missing |
| `imgs/81sQE5M5HhL._AC_SY200_.jpg` | Deal card image | Missing |
| `imgs/9171uzu8PEL._AC_SY200_.jpg` | Deal card image | Missing |
| `imgs/Fragrance_1x._SY116_CB563150139_.jpg` | Deal card image | Missing |
| `imgs/710yBz6hfUL._AC_SY200_.jpg` | Deal card image | Missing |

Some paths are used multiple times in the page. The table records unique paths, not the total number of HTML occurrences.

## 3. Remote resource categories

The current page also references remote resources for:
- Hero carousel images hosted on an Amazon media domain.
- A logo image hosted by a third-party image site.
- Location, dropdown, search, and flag imagery hosted by third parties.
- Font Awesome CSS hosted through a CDN.
- Google Fonts families imported by the stylesheet.

These requests are not bundled into the repository. They can fail, change, or be removed independently of the source code. Their presence in HTML does not prove permission to redistribute them.

## 4. Asset approval register

Before adding a local file, record:

| Field | Required information |
|---|---|
| Repository path | Exact path committed to Git |
| Display name | Human-readable asset name |
| Page location | Selector, card, or section using it |
| Source | Original creator or source URL |
| Rights basis | Licence name or written permission |
| Attribution | Exact notice required, if any |
| Modification | Whether cropping, resizing, or editing is allowed |
| Alternative text | Informative description or reason for decorative status |
| Review date | Date the rights and file were checked |

Do not invent a licence field or use a generic MIT project licence as permission for third-party images.

## 5. Recommended remediation process

1. Review which image slots are still needed.
2. Select original artwork or assets with explicit redistribution rights.
3. Confirm the asset can be stored and redistributed in a public Git repository.
4. Save the file under a predictable local directory.
5. Use a filename that describes the content rather than copying an opaque retailer identifier.
6. Update the HTML reference and alternative text.
7. Add the asset to the rights register.
8. Run `python scripts/check_html.py`.
9. Review the page in a browser and check image dimensions, cropping, and responsive behaviour.
10. Update the README and changelog if the visual change is material.

## 6. Image quality guidance

- Prefer modern, appropriately compressed formats where supported by the target browsers.
- Provide dimensions to reduce layout shifts.
- Avoid oversized source images for small card thumbnails.
- Preserve aspect ratio unless intentional cropping is part of the design.
- Use descriptive filenames and meaningful alternative text.
- Do not embed screenshots of unrelated websites or third-party product pages without permission.

## 7. Current release implication

The missing local image paths are a known visual defect. A successful JavaScript test run does not repair these assets. Any release should either resolve the references or explicitly disclose the missing images.
