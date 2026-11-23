from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_payments_invoice_book_foreigntext import RmErpPaymentsInvoiceBookForeigntext


T = TypeVar("T", bound="RmErpPaymentsInvoiceBook")


@_attrs_define
class RmErpPaymentsInvoiceBook:
    """
    Attributes:
        field_foreigntext (RmErpPaymentsInvoiceBookForeigntext | Unset):
        a_nr (str | Unset):
        belegart (str | Unset):
        faellig_datum (int | Unset):
        id (int | Unset):
        invoice_amount (float | Unset):
        kommentar (str | Unset):
        kost_awkz (str | Unset):
        leitwegid (str | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        rechnungs_datum (int | Unset):
        rechnungs_eingangs_datum (int | Unset):
        rechnungs_nummer (str | Unset):
        skonto_faellig_datum (int | Unset):
        skonto_kennz (str | Unset):
        skonto_satz (float | Unset):
        verarbeitung_status (int | Unset):
        vertrags_betrag (float | Unset):
        vertrags_waehrungs_kennzeichen (str | Unset):
        z_name (str | Unset):
        zahlbetrag (float | Unset):
        zahlungsbedingungen (str | Unset):
    """

    field_foreigntext: RmErpPaymentsInvoiceBookForeigntext | Unset = UNSET
    a_nr: str | Unset = UNSET
    belegart: str | Unset = UNSET
    faellig_datum: int | Unset = UNSET
    id: int | Unset = UNSET
    invoice_amount: float | Unset = UNSET
    kommentar: str | Unset = UNSET
    kost_awkz: str | Unset = UNSET
    leitwegid: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    rechnungs_datum: int | Unset = UNSET
    rechnungs_eingangs_datum: int | Unset = UNSET
    rechnungs_nummer: str | Unset = UNSET
    skonto_faellig_datum: int | Unset = UNSET
    skonto_kennz: str | Unset = UNSET
    skonto_satz: float | Unset = UNSET
    verarbeitung_status: int | Unset = UNSET
    vertrags_betrag: float | Unset = UNSET
    vertrags_waehrungs_kennzeichen: str | Unset = UNSET
    z_name: str | Unset = UNSET
    zahlbetrag: float | Unset = UNSET
    zahlungsbedingungen: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        a_nr = self.a_nr

        belegart = self.belegart

        faellig_datum = self.faellig_datum

        id = self.id

        invoice_amount = self.invoice_amount

        kommentar = self.kommentar

        kost_awkz = self.kost_awkz

        leitwegid = self.leitwegid

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        rechnungs_datum = self.rechnungs_datum

        rechnungs_eingangs_datum = self.rechnungs_eingangs_datum

        rechnungs_nummer = self.rechnungs_nummer

        skonto_faellig_datum = self.skonto_faellig_datum

        skonto_kennz = self.skonto_kennz

        skonto_satz = self.skonto_satz

        verarbeitung_status = self.verarbeitung_status

        vertrags_betrag = self.vertrags_betrag

        vertrags_waehrungs_kennzeichen = self.vertrags_waehrungs_kennzeichen

        z_name = self.z_name

        zahlbetrag = self.zahlbetrag

        zahlungsbedingungen = self.zahlungsbedingungen

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if a_nr is not UNSET:
            field_dict["aNr"] = a_nr
        if belegart is not UNSET:
            field_dict["belegart"] = belegart
        if faellig_datum is not UNSET:
            field_dict["faelligDatum"] = faellig_datum
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_amount is not UNSET:
            field_dict["invoiceAmount"] = invoice_amount
        if kommentar is not UNSET:
            field_dict["kommentar"] = kommentar
        if kost_awkz is not UNSET:
            field_dict["kostAwkz"] = kost_awkz
        if leitwegid is not UNSET:
            field_dict["leitwegid"] = leitwegid
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if rechnungs_datum is not UNSET:
            field_dict["rechnungsDatum"] = rechnungs_datum
        if rechnungs_eingangs_datum is not UNSET:
            field_dict["rechnungsEingangsDatum"] = rechnungs_eingangs_datum
        if rechnungs_nummer is not UNSET:
            field_dict["rechnungsNummer"] = rechnungs_nummer
        if skonto_faellig_datum is not UNSET:
            field_dict["skontoFaelligDatum"] = skonto_faellig_datum
        if skonto_kennz is not UNSET:
            field_dict["skontoKennz"] = skonto_kennz
        if skonto_satz is not UNSET:
            field_dict["skontoSatz"] = skonto_satz
        if verarbeitung_status is not UNSET:
            field_dict["verarbeitung_status"] = verarbeitung_status
        if vertrags_betrag is not UNSET:
            field_dict["vertragsBetrag"] = vertrags_betrag
        if vertrags_waehrungs_kennzeichen is not UNSET:
            field_dict["vertragsWaehrungsKennzeichen"] = vertrags_waehrungs_kennzeichen
        if z_name is not UNSET:
            field_dict["zName"] = z_name
        if zahlbetrag is not UNSET:
            field_dict["zahlbetrag"] = zahlbetrag
        if zahlungsbedingungen is not UNSET:
            field_dict["zahlungsbedingungen"] = zahlungsbedingungen

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_payments_invoice_book_foreigntext import RmErpPaymentsInvoiceBookForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpPaymentsInvoiceBookForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpPaymentsInvoiceBookForeigntext.from_dict(_field_foreigntext)

        a_nr = d.pop("aNr", UNSET)

        belegart = d.pop("belegart", UNSET)

        faellig_datum = d.pop("faelligDatum", UNSET)

        id = d.pop("id", UNSET)

        invoice_amount = d.pop("invoiceAmount", UNSET)

        kommentar = d.pop("kommentar", UNSET)

        kost_awkz = d.pop("kostAwkz", UNSET)

        leitwegid = d.pop("leitwegid", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        rechnungs_datum = d.pop("rechnungsDatum", UNSET)

        rechnungs_eingangs_datum = d.pop("rechnungsEingangsDatum", UNSET)

        rechnungs_nummer = d.pop("rechnungsNummer", UNSET)

        skonto_faellig_datum = d.pop("skontoFaelligDatum", UNSET)

        skonto_kennz = d.pop("skontoKennz", UNSET)

        skonto_satz = d.pop("skontoSatz", UNSET)

        verarbeitung_status = d.pop("verarbeitung_status", UNSET)

        vertrags_betrag = d.pop("vertragsBetrag", UNSET)

        vertrags_waehrungs_kennzeichen = d.pop("vertragsWaehrungsKennzeichen", UNSET)

        z_name = d.pop("zName", UNSET)

        zahlbetrag = d.pop("zahlbetrag", UNSET)

        zahlungsbedingungen = d.pop("zahlungsbedingungen", UNSET)

        rm_erp_payments_invoice_book = cls(
            field_foreigntext=field_foreigntext,
            a_nr=a_nr,
            belegart=belegart,
            faellig_datum=faellig_datum,
            id=id,
            invoice_amount=invoice_amount,
            kommentar=kommentar,
            kost_awkz=kost_awkz,
            leitwegid=leitwegid,
            lock_version=lock_version,
            obj_guid=obj_guid,
            rechnungs_datum=rechnungs_datum,
            rechnungs_eingangs_datum=rechnungs_eingangs_datum,
            rechnungs_nummer=rechnungs_nummer,
            skonto_faellig_datum=skonto_faellig_datum,
            skonto_kennz=skonto_kennz,
            skonto_satz=skonto_satz,
            verarbeitung_status=verarbeitung_status,
            vertrags_betrag=vertrags_betrag,
            vertrags_waehrungs_kennzeichen=vertrags_waehrungs_kennzeichen,
            z_name=z_name,
            zahlbetrag=zahlbetrag,
            zahlungsbedingungen=zahlungsbedingungen,
        )

        rm_erp_payments_invoice_book.additional_properties = d
        return rm_erp_payments_invoice_book

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
